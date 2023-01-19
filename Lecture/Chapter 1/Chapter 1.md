# CS305 Chapter 1

我最近想先后把22春季学习的计算机网络和操作系统的知识点重新整理，重新学一遍。一方面是自己当时确实学的不咋地，另一方面也是想打牢基础，以后工作的时候会有用。

教计算机网络的Prof.李卓钊人真的非常好，人很可爱，教得也好，强烈推荐大一的学弟学妹们选他的Java，大二大三的同学选他的创新实验和计算机网络！

据我上学期的印象，这门课东西非常多，且非常杂，需要软硬件结合，对大家的理论和实践都是很大的考验。

## Part 1. Overview（重要）

计算机网络一共分为五层体系结构，教材采用的讲解策略是自顶向下讲。

```
【考题】五层体系结构的名称？
【答案】Application, Transport, Network, Link, Physical
```

有几个需要**重点理解**但不用背的相关概念：

- host: 网络上的主机，一般是运行应用程序的电子设备和服务器，如手机，电脑等等。PPT里面有一个`edge`，我当时没太懂，以为是数据结构中图里面的`edge`，但注意这个`edge`的意思是边缘（是中央的反义词），而不是边，意思就是说网络上host中的电子设备是在整个网络体系中最边缘化的位置。

【个人理解】host可以理解为图数据结构中的顶点。

- packet switches：交换包，就是说路由器，交换机，主机等等设备之间发送数据。因为数据交换都不是直接交换的，需要以包为单位。

【个人理解】packet是数据交换的基本单位。这个应该很容易理解。

- communication links：链路指的是数据过程中的传播媒介，如光纤、铜缆、卫星等等。

【个人理解】links可以理解为图数据结构中的边。

- networks：路由器，设备，链路

【个人理解】networks可以理解为图数据结构中的子图（图的一部分）。

因此后面有一个`Internet: network of networks`也就不难理解了。

- protocol：协议。控制消息收发的规则。

【个人理解】这个也比较容易理解。消息收发需要符合一定的规则，这与人与人之间沟通需要符合一定的语言和语法是类似的。

后面有定义：Protocols定义了消息收发的format和order，以及消息传输时的行为。

- Internet standard：网络体系的相关标准

【个人理解】**RFC**是一系列以编号排定的文件。文件收集了有关互联网相关信息，以及UNIX和互联网社区的软件文件。

**IRTF**是Internet工程任务组（Internet Engineering Task Force），是推动Internet标准规范制定的最主要的组织。

从服务功能的角度来说，Internet为应用程序提供了服务的**编程接口**，允许用户进行数据的收发。

## Part 2. Network Edge（网络边缘）

网络体系结构：
- 边缘：客户端的应用程序（host的一部分）。host还有一个部分叫做server（服务器），一般位于数据的中心。
- 连接：网络和电子设备之间需要物理媒介，可以是有线的，也可以是无线的。
- 中心：相互连接的路由器

网络设备的两个主要考虑因素：

- 带宽：传输速度，多少bit一秒
- 共享/专用

### 访问网络的几种方法

- 方法1：Cable Network

特性：频分复用。不同的通道传输不同频率的信号。

物理媒介：HFC（混合光纤同轴电缆）。具有上传/下载速度不对称的特性（这是从用户行为的角度考虑的，大多数时候都会占用下载带宽而不会占用上传带宽）。


- 方法2：DSL（数字用户电路）

特性：上传和下载带宽都比较小。上传一般不超过1Mbps，下载一般不超过10Mbps。

物理媒介：使用已有的电话线，传输到中央DSLAM（数字用户线接入复用器）。其中数据走网络途径，声音走电话线途径。

- 方法3：无线共享网络

无线共享网络通过路由器连接到整个网络体系。分为局域网和广域网两种类型。

其中以太网是无线共享网络的主流实现应用。

### Host（主机）

主机发送数据的流程：
- 接收应用程序信息
- 拆分成更小的每个长度为L bits的chunks（又名packets）
- 以传输速度R进行传输（R又名带宽，容量等等）

```
Transmission delay = L/R

L 单位是bits
R 单位是bits/sec
```

### Physical Media（物理媒介）

有几个重要概念：

- bits：传播过程的最小单位
- physical link：传播过程的物理媒介
- guided media：固体介质，主要是实现有向传播，如铜，光纤，双绞线（TP）等等
- unguided media：自由传播介质，会做全空间任意的传播，如无线电等等

#### 双绞线（TP）

两根绝缘铜导线绑在一起，实现不同频道的传输。

#### 同轴电缆

两个同心铜导体放在电缆中，主要功能有：
- 信号双向传播
- 多通道传输
- 混合光纤同轴电缆

#### 光纤

使用玻璃光纤传输光脉冲信号，一个信号仅传输一个bit。特性有高速传输和低错误率。

低错误率的原因有：
- 中继器相隔较远
- 对电磁干扰基本免疫

#### 无线电

使用电磁频谱来传递信号，而无需线性物理媒介。特点是能够双向传播，以及可能受到环境因素的影响。

无线电通信的四种类型：
- 地面微波
- 局域网（LAN）
- 广域网
- 卫星通讯

## Part 3. Protocol layers, service models

计算机网络的协议栈分五层：
- application：IMAP，SMTP，HTTP
- transport：TCP，UDP
- network：IP
- link：以太网，PPP
- physical：wire

课件上有一个很好的例子，解释了五层网络体系的作用，简单归纳一下：

- physical：通讯介质
- link：和邻居通讯，主流代表硬件是交换机（Switch)
- network：使用IP地址，子网和子网掩码在网络中定位通讯路径，主流代表硬件是路由器（Router）
- transport：数据的收发与重组，提供进程在逻辑上的网络通讯能力（也就是做一层抽象，上层不关心底层的原理）
- application：网络应用支持

## Part 4. Network edge: hosts, access network, physical media

请见Part 2.

## Part 5. Network core: packet/circuit switching, internet structure

网络核心的本质是多个相连路由器组成的网络。

### Packet Switching

包交换：主机将应用程序的消息拆分成packet（也称chunk）进行传输。

有三个重要的知识点：

- Transmission Delay(L/R)

（此处应避免写中文，中文容易造成混淆）

消耗L/R的时间，在带宽为R bps的连路上传输L-bit的数据包

后面会有一个解释，这个可以理解为汽车在收费站里上接受检查并出站的时间。

- Store and Forward

包必须整个都到达路由器后才能进行下一次传输

- Queueing delay, loss

如果 数据到达路由器的速度 > 路由器向外发送数据的速度：

1. 到达的数据包会排队，在队列中等待向外传输，等待的时间就是queueing delay

2. 如果路由器的缓存满了，那么再新来的包都会被丢弃，也就触发了loss

![image](https://user-images.githubusercontent.com/64548919/212837796-b4d8afc0-d371-434d-91ba-91ad835bb3b3.png)

### Two key network-core functions

两个主要的function是routing和forwarding。

- Routing(路由)是global的，需要相应的路由算法支持，主要是决定包走什么路径到达destination。
- Forwarding(转发)是local的，主要在路由器内部决定转发到哪个端口。

### Packet Switching和Circuit Switching

#### Circuit Switching基本结构
Circuit Switching（电路交换）中，通讯资源的基本单元是Circuit，也就是链路。

当一个链路被占用的时候，无论传输速度有多低（甚至空闲了），只要没有被释放，就会一直处于占用状态而不能给其他的机器使用，会造成资源浪费。

因此，这和我们打电话的原理是比较类似的（比如说，两个人打电话即使互相不说话，那电话的通信资源也不能释放），在传统的电话中普遍使用的都是这个方法。

#### Circuit Switching中的FDM和TDM

电路交换中主要有两种多路复用的方法以增加资源利用率：时分复用和频分复用。

**频分复用**

把链路分成多个频段，每个用户可以用不同的频段做传播。

![image](https://user-images.githubusercontent.com/64548919/212840460-d32a4118-6d12-4b73-a0b1-7db492719f4c.png)

**时分复用**

将时间分割成很多个时间间隔，每个用户轮流使用这些时间间隔。

![image](https://user-images.githubusercontent.com/64548919/212840598-408530f5-401a-4d73-be39-08105fc6a143.png)

网络通讯基本不使用这种方法，原因是：

1. 用户带宽使用率普遍不高，大多数时候是空闲
2. 用户人数过多
3. 过多用户同时活跃使用的概率太低

Packet Switching
- 可以有效处理间歇性的数据传输
- 有可能会导致超额拥塞问题

### Internet Structure

- 主机需要通过ISP（网络服务提供商）连接到互联网。
- ISP之间需要能够相互连通，这样任意两个主机可以发送数据给对方。
- ISP之间可以直接连通，或者通过IXP连通

![image](https://user-images.githubusercontent.com/64548919/212841945-0ad18d61-72b8-4383-8e20-62626c818601.png)

## Part 6. Performance: loss, delay, throughput

包传送延迟的主要原因：路由器收包速度>发包速度就会触发排队等待

包丢失的主要原因：环境影响+路由器缓冲区满触发丢包

### 包传送延迟的4个主要影响因素

![image](https://user-images.githubusercontent.com/64548919/212843574-98361416-7279-4fba-9425-04cc77eb8f5b.png)

- d_proc基本可以忽略不计

- d_queue是等待时间。主要由L,a和R决定，要考虑La/R。a是包的平均到达比率。影响关系见下图。当La/R>1的时候，就会进入【无限拥堵】状态，预期的等待时间是无限长！

![image](https://user-images.githubusercontent.com/64548919/212845327-661794a8-812a-425a-9dff-71cb4674160a.png)

- d_trans = L/R，其中L是包的长度(单位bit)，R是transmission rate(单位bps)。这个可以理解为汽车在高速收费站中完成检查并驶出的时间，因为这个和包本身大小有关。

- d_prop = d/s，其中d是物理链路的长度，s是传输速度（一般是2*10^8 m/s）。这个可以理解为汽车在高速路上行驶的时间，因为这个和物理链路的长度有关。

### 包丢失的主要因素

路由器的缓冲区所构成队列，大小是有限的。

如果队列满了，那么新来的包就会被丢弃，触发丢包现象。

丢失的包有可能会被前一个节点重传，被源节点重传，或者根本不重传。

### 吞吐量

从sender到receiver的发包速度。
- 即时：瞬时的发送速度
- 平均：一段时间的发送速度

**瓶颈链路**

整个链路的收发速度由中间的最小吞吐量决定。如下图的吞吐量是R_s:

![image](https://user-images.githubusercontent.com/64548919/212847462-39760569-ffe2-4af1-a067-078ad97682d4.png)

下图的吞吐量是min{R_s, R_c, R/10}

![image](https://user-images.githubusercontent.com/64548919/212847542-aea3c7b4-181e-4931-add4-902dd39cca30.png)

## Part 7. Security

- DoS(拒绝服务攻击)：使用大量发包的手段，使得目标机器本身的服务不可用

- Packet Sniffing(数据包嗅探)：中途抓取网络上的流量包，并转发到hacker的主机上

- IP spoofing(IP欺骗)：伪造IP地址以冒充其他人身份，并发送恶意信息。

## Part 8. History