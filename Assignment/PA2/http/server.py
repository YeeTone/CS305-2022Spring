import asyncio
from urllib.parse import unquote

keys = ('method', 'path', 'Range')


'''

以下三个变量：
弹幕发送时间戳————弹幕颜色、弹幕大小、弹幕内容的映射关系
'''


Time_DanmakuColor_Mapping = {}
Time_DanmakuSize_Mapping = {}
Time_DanmakuContent_Mapping = {}

'''
http头部信息，未作修改
'''
class HTTPHeader:
    """
        HTTPHeader template, you can use it directly
    """

    def __init__(self):
        self.headers = {key: None for key in keys}
        self.version = '1.0 '
        self.server = 'Tai'
        self.contentLength = None
        self.contentRange = None
        self.contentType = None
        self.location = None
        self.range = None
        self.state = None

    def parse_header(self, line):
        fileds = line.split(' ')
        if fileds[0] == 'GET' or fileds[0] == 'POST' or fileds[0] == 'HEAD':
            self.headers['method'] = fileds[0]
            self.headers['path'] = fileds[1]
        fileds = line.split(':', 1)
        if fileds[0] == 'Range':
            start, end = (fileds[1].strip().strip('bytes=')).split('-')
            self.headers['Range'] = start, end
        if fileds[0] == 'Content-Length':
            self.headers['Content-Length'] = fileds[1].strip()

    def set_version(self, version):
        self.version = version

    def set_location(self, location):
        self.location = location

    def set_state(self, state):
        self.state = state

    def set_info(self, contentType, contentRange):
        self.contentRange = contentRange
        self.contentType = contentType

    def set_range(self):
        start, end = self.headers['Range']
        contentRange = int(self.contentRange)
        if start == '':
            end = int(end)
            start = contentRange - end
            end = contentRange - 1
        if end == '':
            end = contentRange - 1
        start = int(start)
        end = int(end)
        self.contentLength = str(end - start + 1)
        self.range = (start, end)

    def get(self, key):
        return self.headers.get(key)

    def message(self):  # Return response header
        return 'HTTP/' + self.version + self.state + '\r\n' \
               + ('Content-Length:' + self.contentLength + '\r\n' if self.contentLength else '') \
               + ('Content-Type:' + 'text/html' + '; charset=utf-8' + '\r\n' if self.contentType else '') \
               + 'Server:' + self.server + '\r\n' \
               + ('Accept-Ranges: bytes\r\n' if self.range else '') \
               + ('Content-Range: bytes ' + str(self.range[0]) + '-' + str(
            self.range[1]) + '/' + self.contentRange + '\r\n' if self.range else '') \
               + ('Location: ' + self.location + '\r\n' if self.location else '') \
               + 'Connection: close\r\n' + '\r\n'


async def dispatch(reader, writer):
    # Use reader to receive HTTP request
    # Writer to send HTTP request
    httpHeader = HTTPHeader()
    while True:
        data = await reader.readline()
        message = data.decode()
        httpHeader.parse_header(message)
        if data == b'\r\n' or data == b'':
            break

    if httpHeader.get('method') == 'GET':
        # TODO: handle get request with different situation: GET PAGE and GET NEWDANMAKUS
        if httpHeader.get('path') == '/': # 自带的，没做修改
            httpHeader.set_state('200 OK')
            writer.write(httpHeader.message().encode(encoding='utf-8'))  # construct 200 OK HTTP header
            html_page = open("danmu.html", encoding='utf-8')
            contents = html_page.readlines()
            homepage = ''
            for e in contents:
                homepage += e
            writer.write(homepage.encode())  # Response for GET PAGE
        elif '/getDanmaku' in httpHeader.get('path'): # 自定义的获取弹幕内容信息
            latestTime = int(httpHeader.get('path').split('/getDanmaku?latestTime=')[1])
            httpHeader.set_state('200 OK')
            writer.write(httpHeader.message().encode(encoding='utf-8'))

            returnedDanmaku = ''
            # 一次性获取所有的弹幕内容，格式为Color|||Size|||Content|||TimeStamp
            for k in Time_DanmakuSize_Mapping.keys():
                returnedDanmaku += Time_DanmakuColor_Mapping[k] + '|||' + Time_DanmakuSize_Mapping[k] + '|||' + \
                                   Time_DanmakuContent_Mapping[k] + '|||' + k
                returnedDanmaku += '\n'
            writer.write(returnedDanmaku.encode())
    elif httpHeader.get('method') == 'POST':
        # TODO: handle post request with given parameters
        httpHeader.set_state('200 OK')
        writer.write(httpHeader.message().encode(encoding='utf-8'))  # construct 200 OK HTTP header

        body = await reader.read(int(httpHeader.headers['Content-Length']))
        body = body.decode()
        body = unquote(body)

        body = body.split('value=')[1]

        body = body.split('|||')
        '''
        将前端传回的数据做键为时间的映射处理
        '''
        Time_DanmakuColor_Mapping[body[3]] = body[0]
        Time_DanmakuSize_Mapping[body[3]] = body[1]
        Time_DanmakuContent_Mapping[body[3]] = body[2]

    writer.close()

'''
未作修改
'''
if __name__ == '__main__':
    port = 8765
    loop = asyncio.get_event_loop()
    co_ro = asyncio.start_server(dispatch, '127.0.0.1', port, loop=loop)
    server = loop.run_until_complete(co_ro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
