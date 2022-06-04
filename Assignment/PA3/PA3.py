import os
import sys
from queue import Queue

allIPV4AddressInterfaces = []
allRouters = []
allHosts = []

ipv4NodeMapping = {}

subnets = {}

# Reference: https://blog.csdn.net/sinat_29957455/article/details/121634949
# 借鉴了这个地方的代码，主要用于dijkstra的时候关闭路径的输出流
class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


class NetworkInterface(object):

    def __init__(self, addr_prefix: str):
        ss = addr_prefix.split('/')
        self.address = None
        self.prefix = int(ss[1])
        self.string = addr_prefix
        self.handleAddress(ss[0])

    def handleAddress(self, original: str):
        split = original.split('.')
        li = []
        for k in split:
            li.append(bin(int(k)).replace('0b', '').zfill(8))
        self.address = str.join('.', li)

        connected = str.join('', li)
        finalPrefixForMapping = ''
        for i in range(0, self.prefix):
            finalPrefixForMapping += connected[i]
        if finalPrefixForMapping in subnets.keys():
            subnets[finalPrefixForMapping].append(self)
        else:
            subnets[finalPrefixForMapping] = [self]

    def __str__(self):
        return self.string


class NetworkNode:

    def __init__(self, interfaceString: str, isRouter: bool):
        self.isRouter = isRouter
        self.interfaces = []
        self.neighbors = []
        self.handleInterfaceString(interfaceString)

    def handleInterfaceString(self, interfaceString: str):
        interfaceString = interfaceString.replace('(', '').replace(')', '')
        interfaceString = interfaceString.replace('\'', '')
        strings = interfaceString.split(',')
        for s in strings:
            self.interfaces.append(NetworkInterface(s))
            if self.isRouter:
                allIPV4AddressInterfaces.remove(s)
            ipv4NodeMapping[s] = self

    def addNeighborEdge(self, n):
        self.neighbors.append(n)

    def __str__(self):
        s = [str(k) for k in self.interfaces]
        return str.join(' ', s) + ' ' + str(self.isRouter)


class NetworkEdge(object):
    def __init__(self, edgeString: str):
        self.node1 = None
        self.node2 = None
        self.interfaceValue1 = None
        self.interfaceValue2 = None
        self.cost = 0
        self.handleEdgeString(edgeString)

    def handleEdgeString(self, es: str):
        es = es.replace('(', '').replace(')', '')
        es = es.replace('\'', '')
        values = es.split(',')
        self.interfaceValue1 = values[0]
        self.interfaceValue2 = values[1]
        self.node1 = ipv4NodeMapping[values[0]]
        self.node2 = ipv4NodeMapping[values[1]]
        self.cost = int(values[2])
        self.node1.addNeighborEdge(self)
        self.node2.addNeighborEdge(self)

    def __str__(self):
        return "[{}:{}]".format(self.__class__.__name__, self.gatherAttrs())

    def gatherAttrs(self):
        return ",".join("{}={}"
                        .format(k, getattr(self, k))
                        for k in self.__dict__.keys())


def handleFirstLine(firstLine):
    global allIPV4AddressInterfaces
    allIPV4AddressInterfaces = firstLine.split(' ')


def handleSecondLine(secondLine: str):
    allRoutersInfo = secondLine.split(' ')

    for rt in allRoutersInfo:
        n = NetworkNode(rt, True)
        allRouters.append(n)
    allIPV4Clone = allIPV4AddressInterfaces.copy()
    for rest in allIPV4Clone:
        allHosts.append(NetworkNode(rest, False))
        allIPV4AddressInterfaces.remove(rest)


def handleThirdLine(thirdLine: str):
    allEdgeInfo = thirdLine.split(' ')
    for ei in allEdgeInfo:
        NetworkEdge(ei)


def dijkstra(srcNode, dstNode):
    src = ipv4NodeMapping[srcNode]
    dst = ipv4NodeMapping[dstNode]

    q = Queue()
    costFromSrc = {ipv4NodeMapping[k]: 999999999 for k in ipv4NodeMapping.keys()}
    father = {ipv4NodeMapping[k]: None for k in ipv4NodeMapping.keys()}
    confirmed = {ipv4NodeMapping[k]: False for k in ipv4NodeMapping.keys()}

    fatherEdge = {ipv4NodeMapping[k]: None for k in ipv4NodeMapping.keys()}

    confirmed[src] = True
    costFromSrc[src] = 0
    q.put(src)

    while not q.empty():
        firstPoll = q.get()
        for n in firstPoll.neighbors:
            if n.node1 is firstPoll:
                to = n.node2
            else:
                to = n.node1
            if costFromSrc[to] > costFromSrc[firstPoll] + n.cost:
                costFromSrc[to] = costFromSrc[firstPoll] + n.cost
                q.put(to)
                father[to] = firstPoll
                fatherEdge[to] = n

        pass

    current = dst
    preInterface = dstNode

    resultStack = []
    cost = 0

    resultCurrent = dst

    while current is not None:
        if fatherEdge[current] is not None:
            # if preInterface == str(fatherEdge[current].interfaceValue1):
            #     print(preInterface + '<-' + str(fatherEdge[current].interfaceValue2))
            # else:
            #     print(preInterface + '<-' + str(fatherEdge[current].interfaceValue1))
            if ipv4NodeMapping[fatherEdge[current].interfaceValue1] == ipv4NodeMapping[preInterface]:
                preInterface = fatherEdge[current].interfaceValue2
                lastInterface = fatherEdge[current].interfaceValue1
            else:
                preInterface = fatherEdge[current].interfaceValue1
                lastInterface = fatherEdge[current].interfaceValue2
                # print(ipv4NodeMapping)
                # print('Failed!')
            resultStack.append(lastInterface)
            resultStack.append(preInterface)
            cost += fatherEdge[current].cost
            resultCurrent = preInterface

        current = father[current]

    outputStrings = []
    while len(resultStack) != 0:
        p = str(resultStack.pop())
        p = p.split('/')[0]
        outputStrings.append(p)
    print(str.join(' ', outputStrings))

    return cost, resultCurrent


def buildSubnet(subnet: str) -> str:
    net = []
    for i in range(0, len(subnet), 8):
        length8 = subnet[i:i + 8]
        while len(length8) != 8:
            length8 += '0'
        net.append(str(int(length8, 2)))

    while len(net) != 4:
        net.append('0')
    return str.join('.', net) + '/' + str(len(subnet))


def to01Prefix(subnet: str) -> str:
    sp = subnet.split('/')
    b, p = sp[0], sp[1]
    sp = b.split('.')
    result = ''
    for s in sp:
        result += bin(int(s)).replace('0b', '').zfill(8)
    return result


def is16Fit(p1: str, p2: str) -> bool:
    for i in range(0, 16):
        if p1[i] != p2[i]:
            return False
    return True


def getAggregation(viaInterface: []):
    for i in range(0, len(viaInterface)):
        for j in range(i + 1, len(viaInterface)):
            prefix1 = to01Prefix(viaInterface[i])
            prefix2 = to01Prefix(viaInterface[j])
            if is16Fit(prefix1, prefix2):
                return i, j
    return None, None


def commonPrefix(p1: str, p2: str) -> int:
    result = 0
    for i in range(0, len(p1)):
        if p1[i] == p2[i]:
            result += 1
        else:
            break
    return result


def agg(valueI: str, valueJ: str) -> str:
    prefixNumber = commonPrefix(to01Prefix(valueI), to01Prefix(valueJ))
    p101 = to01Prefix(valueI)
    result = ''
    for i in range(0, prefixNumber):
        result += p101[i]
    result = buildSubnet(result)
    return result


def aggregation(via: {}):
    for interface in via.keys():
        i, j = getAggregation(via[interface])
        while i is not None and j is not None:
            valueI = via[interface][i]
            valueJ = via[interface][j]
            via[interface].remove(valueI)
            via[interface].remove(valueJ)
            via[interface].append(agg(valueI, valueJ))
            i, j = getAggregation(via[interface])


def table(lineInfo: ()):
    directedConnected = []
    via = {}

    for subnet in subnets.keys():
        subnetBuilt = buildSubnet(subnet)
        isDirectedConnected = False
        minInterface = None
        cost = 999999999
        for singleInterface in subnets[subnet]:
            singleInterface = str(singleInterface)
            for interface in lineInfo:
                with HiddenPrints():
                    if cost > dijkstra(interface, singleInterface)[0]:
                        c, cur = dijkstra(interface, singleInterface)
                        cost = min(cost, c)
                        minInterface = cur
                    if cost == 0:
                        isDirectedConnected = True
                    if isDirectedConnected:
                        break
            if isDirectedConnected:
                break

        if isDirectedConnected:
            directedConnected.append(subnetBuilt)
        else:
            if minInterface in via.keys():
                via[minInterface].append(subnetBuilt)
            else:
                via[minInterface] = [subnetBuilt]

    outputResult(directedConnected, via)
    print('After')
    aggregation(via)
    outputResult(directedConnected, via)


def outputResult(directedConnected: [], via: {}):
    result = []
    for s in directedConnected:
        result.append(s + ' is directly connected')
    for k in via.keys():
        for s in via[k]:
            result.append(s + ' via ' + k.split('/')[0])
    result.sort()
    for s in result:
        print(s)
    result.clear()


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        first = f.readline().replace('\n', '').strip()
        handleFirstLine(first)
        second = f.readline().replace('\n', '').strip()
        handleSecondLine(second)
        third = f.readline().replace('\n', '').strip()
        handleThirdLine(third)
        m = int(f.readline().replace('\n', ''))
        for i in range(0, m):
            line = f.readline().strip().split(' ')
            if line[0] == 'PATH':
                src = line[1].replace('\n', '')
                dst = line[2].replace('\n', '')

                dijkstra(src, dst)
            elif line[0] == 'TABLE':
                info = eval(line[1])
                table(info)
