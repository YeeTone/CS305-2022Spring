# CS305-2022Spring Lab8 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice9-1: DHCP
Open wireshark and set the display filter:

```
dhcp
```

There is no packet now.

![image](https://user-images.githubusercontent.com/64548919/163659169-74280286-fbb6-4e30-80fa-1007c3577ed3.png)


Type the following in the cmd:

```
ipconfig /release
ipconfig /renew
```

We can see there are some DHCP packets:

![image](https://user-images.githubusercontent.com/64548919/163659252-ebce8899-aa06-4546-90ca-42f42d5b1c47.png)

### Q1
For the DHCP request:
- src IP: 0.0.0.0
- dst IP: 255.255.255.255


### Q2

### Q3
Least Time:

![image](https://user-images.githubusercontent.com/64548919/163659985-6450c9b6-7a92-4a82-96c6-4cdc98da469c.png)

Its value is 259200s. The DHCP packet type is Offer.

## Practice9-2: Packet Tracer
