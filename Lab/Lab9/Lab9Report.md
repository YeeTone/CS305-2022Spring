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
- src IP: 0.0.0.0, type: non routerable(未分配地址)
- dst IP: 255.255.255.255, type: Broadcast Address(广播地址)


### Q2
It needs DNS to get the translated IP address so that it can contact with others on the Internet.

### Q3
Least Time:

![image](https://user-images.githubusercontent.com/64548919/163659985-6450c9b6-7a92-4a82-96c6-4cdc98da469c.png)

Its value is 259200s. The DHCP packet type is Offer.

## Practice9-2: Packet Tracer
### Two PC connection
![image](https://user-images.githubusercontent.com/64548919/164364029-5b54043c-6c8e-411f-a7c7-0925a51d1a20.png)

Their ip configuration:

![image](https://user-images.githubusercontent.com/64548919/164364078-d825504c-e0d3-4d4a-9603-1feef7c700a5.png)

![image](https://user-images.githubusercontent.com/64548919/164364111-13b01169-1dfe-4921-9b97-4ccc3d395fd2.png)

Connection test:

![image](https://user-images.githubusercontent.com/64548919/164364166-9a04db89-8e13-4197-8d9b-c58a4f85bafd.png)

![image](https://user-images.githubusercontent.com/64548919/164364200-514077cf-8d71-4bf6-8a83-97ed0b8e22c3.png)

We can see that they could reach each other.

### Two PC & One Route

![image](https://user-images.githubusercontent.com/64548919/164367529-23bd239b-6cc7-4e0f-b937-f62a6dc49106.png)

Their ip configuration:

![image](https://user-images.githubusercontent.com/64548919/164367579-ef2e49f2-54b8-4b67-afbe-6c80fb88f5c9.png)

![image](https://user-images.githubusercontent.com/64548919/164367597-ddac6137-b58c-4fb4-83f7-faacdfb76cff.png)

Router configuration:

![image](https://user-images.githubusercontent.com/64548919/164367637-8b0fce65-8935-4a98-bd75-0cc0b469b7f5.png)

![image](https://user-images.githubusercontent.com/64548919/164367652-86ea7408-1f05-40e8-befe-94a4884aa7c0.png)

- PCs & Router connection test

![image](https://user-images.githubusercontent.com/64548919/164368229-57e1c159-8165-4973-a227-42c3a546c55b.png)

![image](https://user-images.githubusercontent.com/64548919/164368256-4d594da7-8322-46ea-811f-ff5b2530af60.png)

The PC cand contact with the routers correctly.


- Two PC connection test

![image](https://user-images.githubusercontent.com/64548919/164367726-1c17d8ee-1c5d-45d8-a08e-189277df30bc.png)

![image](https://user-images.githubusercontent.com/64548919/164367781-6cb2c5e2-986e-473c-9654-90098f7c3e71.png)

We can see that they could communicate with each other.


