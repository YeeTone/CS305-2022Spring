import socket
import threading
import time

import dns.resolver
from dns import resolver, rdatatype
from dnslib import DNSRecord, QTYPE, DNSHeader, RR, A, CNAME

dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']

"""
这个类的作用是做一个特殊的分支异常处理
"""


class FirstException(Exception):
    def __init__(self):
        pass


'''
这个类的作用是做缓存的管理
domainName_expirationMapping: 域名与过期时间的映射关系，过期时间的计算方法是写入的时间+相应的ttl
domain_responseMapping: 域名与先前的响应的映射关系
domain_canonicalMapping: 域名与canonical name的映射关系
domainName_RNameMapping：域名与RName的映射关系，如www.baidu.com与www.a.shifen.com
'''


class CacheManager:
    def __init__(self):
        self.domainName_expirationMapping = dict()
        self.domainName_responseMapping = dict()
        self.domainName_canonicalMapping = dict()
        self.domainName_RNameMapping = dict()
    '''
    ReadCache 返回域名对应的response对象:
    1. 获取当前时间
    2. 检查域名是否存在
        存在 -> 检查是否过期
            过期 -> 缓存失效，返回None
            未过期 -> 缓存有效，直接返回
        不存在 -> 无对应缓存
    注意此处返回的response对象不能直接用，因为请求的id和response不匹配，会报Warning
    '''


    def readCache(self, domain_name: str):
        currentTime = float(time.time())
        if domain_name in self.domainName_expirationMapping.keys() \
                and domain_name in self.domainName_responseMapping.keys():
            expirationTime = self.domainName_expirationMapping[domain_name]
            if currentTime > expirationTime:
                return None
            else:
                response = self.domainName_responseMapping[domain_name]
                return response
        else:
            return None

    '''
    WriteCache 写对应缓存
    考虑到如果有多次writeCache操作的话，后面的会覆盖前面的，因此这里考虑的是直接覆盖
    注意此处的过期时间的计算使用的是绝对时间，单位是秒，过期时间 = 当前时间 + TTL
    
    '''

    def writeCache(self, domain_name: str, response) -> None:
        # TODO
        self.domainName_RNameMapping[domain_name] = response.rr[0].rname
        self.domainName_canonicalMapping[domain_name] = ReplyGenerator.canonical_hostname[:]
        self.domainName_responseMapping[domain_name] = response
        self.domainName_expirationMapping[domain_name] = float(response.a.ttl) + time.time()


class ReplyGenerator:
    # NOTE: While cannot resolve the corresponding ip or domain name is not found you should send message like this
    #  type.
    canonical_hostname = []
    ttl_list = []

    # ReplyGenerator保存先前对域名的响应和TTL
    # 两个add方法都是做添加操作
    @staticmethod
    def addCanonical(canonical) -> None:
        ReplyGenerator.canonical_hostname.append(canonical)

    @staticmethod
    def addTTL(ttl) -> None:
        ReplyGenerator.ttl_list.append(ttl)

    # 重置响应体中的所有对应信息
    @staticmethod
    def allInitiate() -> None:
        ReplyGenerator.canonical_hostname.clear()
        ReplyGenerator.ttl_list.clear()

    # 这个方法是模板里面自带的，因此不再赘述
    @staticmethod
    def replyForNotFound(income_record):
        header = DNSHeader(id=income_record.header.id, bitmap=income_record.header.bitmap, qr=1)
        header.set_rcode(0)  # 3 DNS_R_NXDOMAIN, 2 DNS_R_SERVFAIL, 0 DNS_R_NOERROR
        record = DNSRecord(header, q=income_record.q)
        return record

    # 先使用提供的replyForA方法，然后包装成对应的响应体
    @staticmethod
    def generalReply(income_record, ip, ttl):
        record_replyForA = ReplyGenerator.replyForA(income_record, ip, ttl)
        reply = record_replyForA.reply(ra=1, aa=1)

        canonical_hostname = ReplyGenerator.canonical_hostname
        ttl_list = ReplyGenerator.ttl_list
        length = len(canonical_hostname)

        for index in range(0, length - 2):
            rr = RR(canonical_hostname[index], QTYPE.CNAME, ttl=ttl_list[index],
                    rdata=CNAME(canonical_hostname[index + 1]))
            reply.add_answer(rr)

        if length >= 2:
            rr = RR(canonical_hostname[length - 2], QTYPE.A, rdata=A(canonical_hostname[length - 1]),
                    ttl=ttl_list[length - 2])
            reply.add_answer(rr)

        parsePack = DNSRecord.parse(reply.pack())
        return parsePack

    # NOTE: This is an example for the reply message with just one rr record of a type.
    # 这个方法是模板里面自带的，因此不再赘述
    @staticmethod
    def replyForA(income_record, ip, ttl):
        r_data = A(ip)
        header = DNSHeader(id=income_record.header.id, bitmap=income_record.header.bitmap, qr=1)
        domain = income_record.q.qname
        query_type_int = QTYPE.reverse.get('A') or income_record.q.qtype
        record = DNSRecord(header, q=income_record.q, a=RR(domain, query_type_int, rdata=r_data, ttl=ttl))
        return record


# 这一整个类是模板里面自带的，没有做任何修改，因此不做过多解释
class DNSServer:
    def __init__(self, source_ip, source_port, ip='127.0.0.1', port=5533):
        self.source_ip = source_ip
        self.source_port = source_port
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))
        self.cache_manager = CacheManager()
        self.dns_handler = DNSHandler(self.source_ip, self.source_port, self.cache_manager)

    def start(self):
        while True:
            message, address = self.receive()
            response = self.dns_handler.handle(message)
            self.reply(address, response)

    def receive(self):
        return self.socket.recvfrom(8192)

    def reply(self, address, response):
        self.socket.sendto(response.pack(), address)


class DNSHandler(threading.Thread):
    # 构造方法是模板自带
    def __init__(self, source_ip: str, source_port: int, cache_manager: CacheManager):
        super().__init__()
        self.source_ip = source_ip
        self.source_port = source_port
        self.LOCAL_DNS_SERVER_IP = '8.8.8.8'
        self.DNS_SERVER_PORT = 53
        self.cache_manager = cache_manager

    def handle(self, message):
        try:
            income_record = DNSRecord.parse(message)
            # 这句话是模板自带的
            # 尝试解析，如果解析失败，那么就返回，不处理（也是防止后续空指针导致crash）
            if income_record is None:
                raise Exception
        except:
            return
        domain_name = str(income_record.q.qname).strip('.')
        cacheManager = self.cache_manager

        # 尝试从内存缓存中读取域名对应的已有response
        # 注意：不能直接返回，因为IP不对应，会报出Warning，最终结果为查询超时
        tryReadingCache = cacheManager.readCache(domain_name=domain_name)
        if tryReadingCache is not None:
            cans = cacheManager.domainName_canonicalMapping[domain_name]
            # 添加响应体头部信息
            if len(cans) != 0 and cans[0] != domain_name:
                cans.insert(0, domain_name)

            # 这里的if分支是想防止空指针导致DNS服务器崩溃（不知道是否有header是None type的实际情况）
            if income_record.header is not None:
                header = DNSHeader(id=income_record.header.id, bitmap=income_record.header.bitmap, qr=1)
                if income_record.q is None:
                    return

                domain = income_record.q.qname
                qType = income_record.q.qtype or QTYPE.reverse.get('A')

                # 以下是在重新包装响应体信息
                record = DNSRecord(header=header, q=income_record.q,
                                   a=RR(domain, qType, rdata=A(cans[len(cans) - 1]), ttl=0))
                if record is None:
                    return
                reply = record.reply()
                length = len(cans)

                for i in range(0, len(cans) - 2):
                    rr = RR(cans[i], QTYPE.CNAME, rdata=CNAME(cans[i + 1]), ttl=tryReadingCache.a.ttl)
                    reply.add_answer(rr)

                if len(cans) >= 2:
                    rr = RR(cans[length - 2], QTYPE.A, rdata=A(cans[length - 1]), ttl=tryReadingCache.a.ttl)
                    reply.add_answer(rr)
                parsePack = DNSRecord.parse(reply.pack())

                print('read from cache')
                return parsePack

        # 如果本地没找到对应缓存，那么就需要走网络查询
        dstIP, dstName = self.query(domain_name, self.source_ip, self.source_port)
        ReplyGenerator.addCanonical(dstIP)

        # 如果没查到，那么就走replyForNotFound，这个一方面是实际功能如此，另一方面出于对空指针的考虑
        if dstIP is None:
            re = ReplyGenerator.replyForNotFound(income_record)
            ReplyGenerator.allInitiate()  # 重置域名和TTL信息
            return re
        else:  # 查到了就保存对应的缓存
            re = ReplyGenerator.generalReply(income_record, dstIP, 0)
            cacheManager.writeCache(domain_name, re)  # 写缓存
            ReplyGenerator.allInitiate()  # 重置域名和TTL信息
            return re

    def query(self, query_name, source_ip, source_port):
        try:
            dnsResolver = resolver.Resolver()
            dnsResolver.flags = 0X0000
            # Get IP address of root server
            server_ip, server_name = self.queryRoot(source_ip, source_port)
            server_port = self.DNS_SERVER_PORT
            dnsResolver.nameservers.clear()
            dnsResolver.nameservers.append(server_ip)

            # 搜索所有可用的server进行后续的dfs搜索
            DNSHandler.addAllIntoDnsResolver(dnsResolver, source_ip, source_port, query_name, isOnlyFirst=True)
            DNSHandler.addAllIntoDnsResolver(dnsResolver, source_ip, source_port, query_name, isOnlyFirst=False)

            return DNSHandler.depth_first_search(self, source_ip, source_port, query_name, dnsResolver)

        except Exception as e:
            return None, None

    '''
    这里是考虑将所有可用信息加入到dnsResolver对象中的nameservers里
    '''

    @staticmethod
    def addAllIntoDnsResolver(dnsResolver, source_ip, source_port, query_name, isOnlyFirst: bool) -> None:

        ans = dnsResolver.resolve(qname=query_name, rdtype=rdatatype.A, source=source_ip,
                                  raise_on_no_answer=False, source_port=source_port)
        re = ans.response
        dnsResolver.nameservers.clear()
        for addis in re.additional:
            if addis is None:
                continue
            if isOnlyFirst:
                server = addis[0]
                if server is not None:
                    dnsResolver.nameservers.append(server.to_text())
            else:
                for server in addis:
                    # print(server)
                    dnsResolver.nameservers.append(server.to_text())

    '''
    深度优先搜索，如果本地缓存过期，或者是没找到，那么就是走此条路线，直到找到为止
    '''

    @staticmethod
    def depth_first_search(dnsHandler, source_ip, source_port, qname, dnsResolver):
        try:
            try:
                answer = dnsResolver.resolve(qname=qname, rdtype=rdatatype.A, source=source_ip,
                                             raise_on_no_answer=False,
                                             source_port=source_port)
                # 特殊的分支处理（其实如果能goto当然更好，但这个库并不在规定范围内）
                # 如果首次查询就失败，那么就回到原先的位置做普通查询
            except Exception as e:
                raise FirstException()
            answerResponse = answer.response
            answerResponseAnswer = answerResponse.answer

            answerResponseAuthority = answerResponse.authority
            if len(answerResponseAnswer) != 0:
                answerResponseAnswer0 = answerResponseAnswer[0]
                rdType = answerResponseAnswer0.rdtype
                if rdType is not None and (rdType == rdatatype.A or rdType == rdatatype.CNAME):
                    if rdType == rdatatype.A:
                        # A 是最后的一个搜索位置，因此就应当是查询到目标结果
                        ReplyGenerator.addTTL(answerResponseAnswer0.ttl)
                        return answerResponseAnswer0[0].to_text(), answerResponseAnswer0.name
                    elif rdType == rdatatype.CNAME:
                        # CNAME是中间分支，需要继续递归查询
                        qname = answerResponseAnswer0[0].to_text()
                        ReplyGenerator.addCanonical(qname)
                        ReplyGenerator.addTTL(answerResponseAnswer0.ttl)
                        # print(dnsResolver.nameservers)
                        return DNSHandler.depth_first_search(dnsHandler=dnsHandler, qname=qname,
                                                             source_ip=source_ip, source_port=source_port,
                                                             dnsResolver=dnsResolver)

            answerResponseAdditional = answerResponse.additional
            # 以下的分支，依次考虑additional，authority和other
            # additional和authority要走继续的dfs查询
            # 注意顺序不能出错，否则会无限递归查询
            if len(answerResponseAdditional) != 0:
                return DNSHandler.buildAdditional(dnsResolver, dnsHandler, qname, source_ip, source_port,
                                                  answerResponseAdditional)
            elif len(answerResponseAuthority) != 0:
                return DNSHandler.buildAuthority(dnsResolver, dnsHandler, qname, source_ip, source_port,
                                                 answerResponseAuthority)
            else:
                return DNSHandler.buildOther(dnsResolver, dnsHandler, qname, source_ip, source_port)
        except FirstException as fe:
            return dnsHandler.query(qname, source_ip, source_port)

        except Exception as e:
            return None, None

    # 构建additional的情况，需要继续dfs
    @staticmethod
    def buildAdditional(dnsResolver, dnsHandler, qname, source_ip, source_port, answerResponseAdditional):
        if dnsResolver is None or dnsResolver.nameservers is None or dnsHandler is None:
            raise Exception
        dnsResolver.nameservers.clear()
        for addi in answerResponseAdditional:
            try:
                if addi is None:
                    raise Exception('None Object!')
                dnsResolver.nameservers.append(addi[0].to_text())
            except Exception as e:
                # print(e.args[0])
                raise e
        return DNSHandler.depth_first_search(dnsHandler=dnsHandler, qname=qname, source_ip=source_ip,
                                             source_port=source_port, dnsResolver=dnsResolver)

    # 构建authority的情况，需要继续dfs
    @staticmethod
    def buildAuthority(dnsResolver, dnsHandler, qname, source_ip, source_port, answerResponseAuthority):
        # 异常空值检查
        if dnsResolver is None or dnsResolver.nameservers is None or dnsHandler is None:
            raise Exception
        queryName_newerVersion = answerResponseAuthority[0][0].to_text()
        if queryName_newerVersion is None:
            raise Exception

        authority_ip, authority_name = dnsHandler.query(query_name=queryName_newerVersion, source_ip=source_ip,
                                                        source_port=source_port)
        # 注意查询后要清空信息，然后重置检查
        dnsResolver.nameservers.clear()
        dnsResolver.nameservers.append(authority_ip)
        return DNSHandler.depth_first_search(dnsHandler=dnsHandler, qname=qname, dnsResolver=dnsResolver,
                                             source_ip=source_ip, source_port=source_port)

    @staticmethod
    def buildOther(dnsResolver, dnsHandler, qname, source_ip, source_port):
        answer = dnsResolver.resolve(qname=qname, rdtype=rdatatype.A, source=source_ip,
                                     raise_on_no_answer=False, source_port=source_port)
        # 异常空值检验，方便单步调试
        if answer is None:
            raise Exception()
        answerResponse = answer.response
        if answerResponse is None:
            raise Exception()
        answerResponseAnswer = answerResponse.answer
        if answerResponseAnswer is None:
            raise Exception()

        # 以下是逐一查询直到有相关的返回结果
        isEmpty = len(answerResponseAnswer) == 0

        while isEmpty:
            if dnsResolver.nameservers is None:
                break

            dnsResolver.nameservers.clear()
            for adds in answerResponse.additional:
                if adds is None:
                    raise Exception
                dnsResolver.nameservers.append(adds[0].to_text())
            answer = dnsResolver.resolve(qname=qname, rdtype=rdatatype.A, source=source_ip,
                                         raise_on_no_answer=False, source_port=source_port)
            if answer is None:
                raise Exception
            answerResponse = answer.response
            if answerResponse is None:
                raise Exception
            answerResponseAnswer = answerResponse.answer
            isEmpty = len(answerResponseAnswer) == 0

        answerResponseAnswer0 = answerResponseAnswer[0]
        return answerResponseAnswer0[0].to_text(), answerResponseAnswer0.name

    '''
    该方法在模板中有，没做过多修改，此处不再赘述
    '''

    def queryRoot(self, source_ip, source_port):
        dns_resolver = resolver.Resolver()
        dns_resolver.flags = 0X0000
        server_name = 'Local DNS Server'
        server_ip = self.LOCAL_DNS_SERVER_IP
        server_port = self.DNS_SERVER_PORT
        dns_resolver.nameservers.clear()
        dns_resolver.nameservers.append(server_ip)

        # Use dns_resolver to query name of root server and receive answerResponse.
        answer = dns_resolver.resolve(qname='', rdtype=rdatatype.NS, source=source_ip, raise_on_no_answer=False,
                                      source_port=source_port)
        answerResponse = answer.response
        query_name = answerResponse.answer[0][0].to_text()

        # Use dns_resolver to query address of root server and receive answerResponse.
        answer = dns_resolver.resolve(qname=query_name, rdtype=rdatatype.A, source=source_ip,
                                      raise_on_no_answer=False, source_port=source_port)
        answerResponse = answer.response
        server_ip = answerResponse.answer[0][0].to_text()
        server_name = answerResponse.answer[0].name

        return server_ip, server_name


if __name__ == '__main__':
    source_ip = input('Enter your ip: ')
    source_port = input('Enter your port: ')
    # source_ip = str('10.26.128.169')
    # source_port = int(55)
    source_ip = str(source_ip)
    source_port = int(source_port)
    local_dns_server = DNSServer(source_ip, source_port)
    dns_handler = DNSHandler(None, None, None)
    root_sever_ip, root_severs = dns_handler.queryRoot(source_ip=source_ip, source_port=source_port)
    print(root_sever_ip)
    print(root_severs)
    local_dns_server.start()
