# CS305-2022Spring Lab8 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice8-1: TCP stream
Open the Wireshark, and start capturing the packets, using filters:

```
ip.addr == 128.119.245.12 && tcp.stream
```

Open command line, and invoke a HTTP request:

```
curl http://gaia.cs.umass.edu/wiresharklabs/alice.txt
```

And we get multiple packets:

![image](https://user-images.githubusercontent.com/64548919/162619486-f8f471e2-a107-4801-a24e-35a987b20941.png)

### Duplicate ACKs
Change filters into this:

```
ip.addr == 128.119.245.12 && tcp.stream && tcp.analysis.duplicate_ack
```

![image](https://user-images.githubusercontent.com/64548919/162619396-dd90e835-501a-454b-8d8a-106bb2bfab93.png)

There is no duplicate ACKs.

### SACK

Select one TCP packets

![image](https://user-images.githubusercontent.com/64548919/162619466-47344a3d-5775-4c97-8029-22823f4ada88.png)

