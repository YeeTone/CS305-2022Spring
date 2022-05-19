# CS305-2022Spring Lab14 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice 14.1

1. Connection:

![30004DC79984031623023F4AD7665751](https://user-images.githubusercontent.com/64548919/169254228-472ba43a-1f49-40c0-bda8-e15c80999ccb.jpg)

2. ping:

![2](https://user-images.githubusercontent.com/64548919/169254287-1c3611e3-d731-460e-b328-90a44c155f00.png)

3. two ways:

![3-1](https://user-images.githubusercontent.com/64548919/169254409-28f83338-7e0c-43b5-9427-d5d434e502db.png)

![3-2](https://user-images.githubusercontent.com/64548919/169254424-10d35a8e-027b-4a64-95a7-fbf61a69d1e9.png)

![3-1-1](https://user-images.githubusercontent.com/64548919/169254450-2898a8b1-3589-4631-9cda-9dcd1c310f0d.png)

4. Mac address table:

![4](https://user-images.githubusercontent.com/64548919/169254522-d9584825-5a33-43f4-b4e8-9bdc727b0d46.png)

(a) 2 items. They are dynamic since their aging is 'Y'.

(b) They belong to the connected PC.
## Practice 14.2

1. display vlan brief

![1](https://user-images.githubusercontent.com/64548919/169255101-10ffef1c-d468-4978-9b4f-d3ed4ac416c7.png)

2. default VLAN:

![2](https://user-images.githubusercontent.com/64548919/169255249-9ffb16bc-548f-43ed-a475-9a05c4758b2e.png)v

There is 1 default vlan. They belong to the 11 port.

3. Create two VLANs: VLAN ‘x’ and VLAN ‘y’ on Layer3 Switch / Router.

![3](https://user-images.githubusercontent.com/64548919/169255442-837e7a64-52f3-4d6c-8abd-4441453541e9.png)

4. Configure the VLANs and interfaces:

![4](https://user-images.githubusercontent.com/64548919/169255495-6ae5e50c-ff77-400f-9305-856e862328b7.png)

5. Setup the connections:

![5-1](https://user-images.githubusercontent.com/64548919/169255552-399fe92c-3d2c-4458-91e6-4ccdfe2ecbc1.png)

They cannot be connected.

6. Configure PCa and PCb with static IP addresses which belong to the same network.

Since we use PC in the lab classroom, they automatically belong to the same network.

7. Is there anyway to make the PCa reachable from PCb without changing the connection? Try and test.

Use ```trunk``` commands.

![7-2](https://user-images.githubusercontent.com/64548919/169255841-6e6a00e4-dcce-4679-bc6a-cd5cc3c33a04.png)

![7-1](https://user-images.githubusercontent.com/64548919/169255859-31b78ea9-c0ae-44ac-b89d-7877932e9c35.png)
