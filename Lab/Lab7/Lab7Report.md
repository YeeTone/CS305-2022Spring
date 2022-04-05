# CS305-2022Spring Lab7 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice7-1: UDP Packet
Select one UDP packet first:

![image](https://user-images.githubusercontent.com/64548919/161696500-120de7c3-6340-443f-99f4-4edb4607b02b.png)

Then open the header:

![image](https://user-images.githubusercontent.com/64548919/161696660-95876ae4-ea67-451c-ac06-a70c84f2e6f6.png)

- (1)There are 4 fields in the headers.
- (2)Names and values
  - Source Port: 64266
  - Destination Port: 53
  - Length: 44
  - Checksum: 0x386f
- (3)Length:
  - Source Port: 2 bytes
  - Destination Port: 2 bytes
  - Length: 2 bytes
  - Checksum: 2 bytes
- (4)MaxLength: 8 bytes since 4 * 2 = 8 bytes.
- (5)Max Destination Port: Consider there are 16 bits in the destination field, the maximum port is 2^16 - 1 = 65535.
- (6)Protocol ID: 17 in decimal, 0x11 in hexadecimal

## Practice7-2: Questions in `Wireshark_TCP_v7.0.pdf`
### Q4. Sequence number
First use display filter to get the ip address of `gaia.cs.umass.edu`:

```
http.host == "gaia.cs.umass.edu"
```

We get the ip address is `128.119.245.12`.

Then use this in the display filter:

```
ip.addr == 128.119.245.12
```

We can get the initial sequence number is 0.

![image](https://user-images.githubusercontent.com/64548919/161708749-7f35c67f-e0b7-495d-a42c-c4a7a26fc84f.png)

### Q5. SYNACK fields
Select one SYNACK packet: 

![image](https://user-images.githubusercontent.com/64548919/161709403-0cbfbf25-539f-4da9-88ce-2770303d56f0.png)

- Sequence number: 0
- Acknowledgement value: 1

![image](https://user-images.githubusercontent.com/64548919/161709851-47a66dd4-3968-4d17-951b-bfe492edad90.png)

- The value is determined by increasing 1 to the initial sequence number.
- The flag is set as (SYN, ACK), to identify the SYNACK segment.

![image](https://user-images.githubusercontent.com/64548919/161710593-b600fbdc-4782-480a-9f75-9cd698e6e813.png)

### Q6. POST
Select one PST packet:

![image](https://user-images.githubusercontent.com/64548919/161713424-d594f154-6d21-4808-af7a-5544c02572a6.png)

Here is the sequence number, it is 1:

![image](https://user-images.githubusercontent.com/64548919/161713386-69f1bfc9-3d0a-4698-8066-e3147c7eed3e.png)

### Q7. POST, TCP, RTT
Consider the first six segments:

![image](https://user-images.githubusercontent.com/64548919/161749366-eef70915-e4ec-4247-ae60-31e7a657b54c.png)

Their sequence numbers are: 1, 982, 2442, 3902, 5362, 6822

Their sent time are: 50.792192s, 52.025106s, 52.296217s, 52.301677s, 52.302.708s, 52.304825s

Their ACK received time are: 50.796298s, 52.296150s, 52.301602s, 52.302651s, 52.304747s, 52.308065s

### Q9. Buffer space
The minimum buffer space is 29200, and maximum is 131328.

![image](https://user-images.githubusercontent.com/64548919/161721309-08dc0708-114c-41aa-aabb-f7593f116703.png)

The lack of receiver buffer space does not throttle the sender.

### Q10 Retransmission
Select one TCP packet with PSH and ACK:

![image](https://user-images.githubusercontent.com/64548919/161745983-e56fdba6-39ec-458f-bb25-34274350fb11.png)

Then consider the Time/Sequence Graph.

![image](https://user-images.githubusercontent.com/64548919/161746036-74ef81a7-fa63-41b1-be5f-0defb2227910.png)

We can see that the sequence number is increased with time. Thus there is no data retransmission. If there is retransmission, the sequence number will have a "local minimum".

### Q12 Throughput
First and last TCP packet:

![image](https://user-images.githubusercontent.com/64548919/161724911-af788ee5-0bfb-49ff-8a71-6eec81645f66.png)

Time = 9.455048 - 3.623846 = 5.831202 s

Amount of data transferred: 1144 - 0 = 1144 bytes

Throughput = 1144 / 5.831202 = 196 bytes/sec
