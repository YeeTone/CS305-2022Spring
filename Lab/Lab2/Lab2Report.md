# CS305-2022Spring Lab2 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice 1: Find Narcissistic Numbers

- **Source Code**
```python
def narcissistic(value: int) -> bool:
    length = len(str(value))
    subs = [int(single) ** length for single in str(value)]
    sum3 = sum(subs)
    del subs
    return sum3 == value


def find_narcissistic_number(start: int, end: int) -> list:
    result = []
    for number in range(start, end + 1, 1):
        if narcissistic(number):
            result.append(number)
    return result


print(' '.join([str(i) for i in find_narcissistic_number(1, 1000000)]))
```
This program can display all the narcissistic numbers from 1 to 1,000,000(including).

- **Commands and Screenshots**

Type this in the command line:
```
python3 narcissistic_number.py
```
And this is the screenshot of the python source code.
![image](https://user-images.githubusercontent.com/64548919/155740310-37b2a345-b4dd-4a2b-a369-7228fb7897e3.png)

## Practice 2: Wireshark & curl

### Problem 2-1
#### Q1
Filter: Capture Filter. Since capture filter can select those packets satisfying the requirements.
#### Q2
##### Step 1: Use display filter to find out the ip address of www.example.com. But unfortunately, we cannot find any packets since we haven't built connection with the destination address.
![image](https://user-images.githubusercontent.com/64548919/155835431-95a08556-a58a-4412-b803-8aef2799cb58.png)

##### Step 2: Type the following in the command line, so that curl can send request via ipv4.
```
curl --ipv4 www.example.com
```
Then it can be seen that the ip address of www.example.com is 93.184.216.34, and localhost is 10.26.128.169.
![image](https://user-images.githubusercontent.com/64548919/155835506-05741722-9af9-4870-a90c-b330f1ab614c.png)

##### Step 3: Add the new capture filter. 
This is the filter requirement:
```
src host 93.184.216.34 and dst host 10.26.128.169
```

##### Step 4: Select a packet we need.
- Packet we select:

![image](https://user-images.githubusercontent.com/64548919/155835622-163cca58-bce2-4360-af8e-bd0046d0cc99.png)

- Source Address

![image](https://user-images.githubusercontent.com/64548919/155835672-8b583197-149f-4afe-807a-f840705fb667.png)

- Source Port

![image](https://user-images.githubusercontent.com/64548919/155835701-262e8174-c6d5-45d9-8725-8c7624a1c4f9.png)

- Destination Address

![image](https://user-images.githubusercontent.com/64548919/155835710-6edb0d5a-514c-4587-8994-26ee9e838f12.png)

- Destination Port

![image](https://user-images.githubusercontent.com/64548919/155835716-e8817e11-5043-47c5-a3a6-cb6e1077b12b.png)

We can find these information:
```
Source Address: 93.184.216.34(5d.b8.d8.22 in hexadecimal)
Source Port: 80(0050 in hexadecimal)
Destination Address: 10.26.128.169(0a.1a.80.a9 in hexadecimal)
Destination Port: 10439(28c7 in hexadecimal)
```

### Problem 2-2
#### Q1
The process of this part is as same as Q2 in Problem 2-1.
So only screenshots and commands will be displayed.

##### Step 1

![image](https://user-images.githubusercontent.com/64548919/155836091-6d0772de-43aa-4ff8-b504-003395be24d9.png)

##### Step 2

```
curl --ipv4 www.baidu.com
```
![image](https://user-images.githubusercontent.com/64548919/155836149-475b0243-e6cc-4030-b8e9-d6b10500fdd9.png)



##### Step 3
- Packet we select:

![image](https://user-images.githubusercontent.com/64548919/155836199-7c0f6b54-1e9c-4038-875e-901fc67cbb41.png)

- Source Address:

![image](https://user-images.githubusercontent.com/64548919/155836220-7a3a7f77-9066-4a0a-9f72-c55b27f4812c.png)

- Source Port:

![image](https://user-images.githubusercontent.com/64548919/155836228-82ea996f-cc9c-40e1-8a2d-1cddc1c2e38a.png)

- Destination Address:

![image](https://user-images.githubusercontent.com/64548919/155836244-c3baac63-3cfa-4366-a400-5f864a4ee19c.png)

- Destination Port:

![image](https://user-images.githubusercontent.com/64548919/155836255-e56f1a5d-6109-4cc3-8c77-607ec45797de.png)

```
Source Address: 14.215.177.39(0e.d7.b1.27 in hexadecimal)
Source Port: 80(0050 in hexadecimal)
Destination Address: 10.26.128.169(0a.1a.80.a9 in hexadecimal)
Destination Port: 10071(2757 in hexadecimal)
```

#### Q2
Comparing the result in Q2 of Problem 2-1 and Q2 of Problem 2-2:

|                     | www.example.com | www.baidu.com  |
|---------------------|-----------------|----------------|
| Source Address      | 93.184.216.34   | 14.215.177.39  |
| Source Port         | 80              | 80             |
| Destination Address | 10.126.128.169  | 10.126.128.169 |
| Destination Port    | 10439           | 10071          |

And we can find that the source port and destination address are identical in the two cases.

## Practice 3: Wireshark & tracert
### Q1
- Step 1: Add capture filter to select those packets whose destination address is www.163.com.
<<<<<<< Updated upstream

```
ip host www.163.com
```
![image](https://user-images.githubusercontent.com/64548919/155871997-2d569638-0c3e-481b-958d-80e370fc20f1.png)



- Step 2: Type the following commands to trace the route:

```
tracert -4 www.163.com
```

![image](https://user-images.githubusercontent.com/64548919/155871695-c2739d23-452b-4189-b208-463822dfa7a7.png)

And we can find those packets with display filter ```icmp```

![image](https://user-images.githubusercontent.com/64548919/155871720-8dd27966-a28b-485c-97d6-504eaab5149d.png)

Reorganize the packet information, group by Info.

**8 echo reply messages**

![image](https://user-images.githubusercontent.com/64548919/155871913-01c79a5e-3afb-4a96-b419-5cd8a739a2fe.png)

**27 time-to-live exceed messages**

![image](https://user-images.githubusercontent.com/64548919/155871934-49434cc2-f1bb-4598-811f-31a7bd270f1f.png)

- Step 3: Reorganize the packet information, order by No.

![image](https://user-images.githubusercontent.com/64548919/155872108-99483cf2-1446-435a-8287-fceadc29905f.png)

We can find the first received 'time-to-live exceed' message number is 60, and the first received 'echo reply' message number is 1090.

![image](https://user-images.githubusercontent.com/64548919/155872384-62bc76e4-034d-4c76-807a-b26b1418ed3e.png)

![image](https://user-images.githubusercontent.com/64548919/155872405-bb8fe71f-aa12-47c0-b4d2-81f517cf6260.png)

- Step 4: Click and see the details.

**First TTL Exceed Source IP Address: 10.10.10.11**

![image](https://user-images.githubusercontent.com/64548919/155872513-a4888b9e-cee2-49b6-99d3-e1bb3e0657d1.png)
  
**First Echo Reply Source IP Address: 10.27.255.254**

![image](https://user-images.githubusercontent.com/64548919/155872581-4191f7f5-6d65-46b8-9027-ca78034eaf0c.png)

### Q2
- Step 1: Use the command to calculate RTT.

```
ping -4 www.164.com
```

![image](https://user-images.githubusercontent.com/64548919/155875655-3771113a-9819-49c1-9044-04c770a7f680.png)

We can see the RTT value is 13ms.

- Step 2: Use wireshark to find RTT of all selected packets.

![image](https://user-images.githubusercontent.com/64548919/155876012-43476e81-b50d-482f-8381-ec0eb5f38bb9.png)

The average value is 0.013430 s = 13.430ms.

We find that this result is almost the same as the command line result.

### Q3

- Step 1: Type the following command in the command line.
=======
```
ip host www.163.com
```

Then type the following commands to trace the route:
>>>>>>> Stashed changes

```
tracert -4 www.163.com
```

<<<<<<< Updated upstream
Then we can find the route of accessing www.163.com.
![image](https://user-images.githubusercontent.com/64548919/155979879-0af26de0-bd45-4524-babf-1b379791550e.png)

- Step 2: Use Wireshark to find the corresponding packet. (We take the second line with ip address 10.23.255.83 as the example)

Use the following display filter:

```
icmp && ip.addr == 10.23.255.83
```

![image](https://user-images.githubusercontent.com/64548919/155980361-0992d79b-1c5f-4222-a269-efb3f127f909.png)

- Step 3: See the packet TTL information.

![image](https://user-images.githubusercontent.com/64548919/155980428-d99fa887-6469-4164-b2f4-7e48bf44532c.png)

We can see the TTL + hop = 254 + 2 = 256, is the constant.

#### Proof
This sum value is constant, because when the ip hops from one address to another, the TTL value will decrease 1 and hop will increase 1.
If the TTL is 0 after decreasing, then the packet will be processed, or loss.
Therefore, the sum will be an constant value.
=======
>>>>>>> Stashed changes
