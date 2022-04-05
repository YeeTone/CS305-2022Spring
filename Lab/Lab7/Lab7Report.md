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
