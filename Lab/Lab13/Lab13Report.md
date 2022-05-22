# CS305-2022Spring Lab13 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice 13.1 
Build network:

![image](https://user-images.githubusercontent.com/64548919/169682710-77fb2a30-536f-4b5c-91eb-824bba3cc24b.png)

1. PC0 pings PC1

![image](https://user-images.githubusercontent.com/64548919/169682919-3f8d8b6f-ca01-405b-b8be-1c22565a0ae8.png)

There is 1 arp message.

After the message is received by router, the router will reply the ARP packet, with the router IP and router MAC address.

2. PC0 pings PC2

![image](https://user-images.githubusercontent.com/64548919/169683120-ca814cc3-ef8a-4cb3-9675-bfbd92336e23.png)

There is no arp entity.

## Practice 13.2

Build LAN:

![image](https://user-images.githubusercontent.com/64548919/169683428-6177e59f-7eba-4ac9-8318-dfefb1982de6.png)

This will not be affected, since PC0 can still reach PC1.

![image](https://user-images.githubusercontent.com/64548919/169683463-826a59ba-df93-4d73-bfc6-153ed35bdb20.png)

Show spanning tree:

- Switch 1:
![image](https://user-images.githubusercontent.com/64548919/169683483-9f561edc-fbc0-4894-b080-f8a11de10389.png)

- Switch 0:

![image](https://user-images.githubusercontent.com/64548919/169683529-928382e9-cff1-44c3-a685-308ee787eccc.png)

We can see the root is switch 0.

After shutdown the Fa0/3 of switch 3:

![image](https://user-images.githubusercontent.com/64548919/169683566-e4b5a625-2843-4c7d-b34c-896d234e99fb.png)

The root is not changed.

![image](https://user-images.githubusercontent.com/64548919/169683577-141d1d54-8a0b-4745-a14c-e585cb48bff7.png)
