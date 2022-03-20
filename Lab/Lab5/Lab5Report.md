# CS305-2022Spring Lab5 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice5-1: Query using ```dig```
**Step 1: Type the following in the command line:**

```
dig www.sina.com.cn +trace
```

This is the screenshot of the output in the command line:

![image](https://user-images.githubusercontent.com/64548919/159166750-34755f96-4ccd-47b5-ad8f-06819128253d.png)

**Step 2: Packet Analysis**

- `RD` and `RA` field in the query:

![image](https://user-images.githubusercontent.com/64548919/159167364-6c0f58f6-cf0d-4b39-8497-42f570ab4cee.png)

We can see the `RD` field is 1 bit `0` and `RA` field is 1 bit `0`.

- Queries from localhost

First use `ipconfig` to get the ip of localhost:

![image](https://user-images.githubusercontent.com/64548919/159167486-e8948fd6-eba2-4f4e-ac2d-8f05fef02a7d.png)

Then use wireshark to collect those data from localhost and to `www.sina.com.cn`. There are 3 quries:

![image](https://user-images.githubusercontent.com/64548919/159167556-d4f8f3f8-ec00-4c53-9f09-35c4cc25018a.png)

Look at their `transaction id`:
![image](https://user-images.githubusercontent.com/64548919/159167654-e42fa326-a554-4fc1-b86f-09cc3b9046ad.png)

![image](https://user-images.githubusercontent.com/64548919/159167662-5c4ecccb-c98d-419f-88d3-9cd4d0aebcfb.png)

![image](https://user-images.githubusercontent.com/64548919/159167681-b315fd59-5e46-4fea-accf-f2d6e20946e3.png)

Their transaction ids are: 0x2483, 0x9254, 0xc3a0. So they do not share the same transaction id.

- Last Response

Considering the last line of the trace result:

![image](https://user-images.githubusercontent.com/64548919/159168793-7c2d768d-d659-420d-8cf4-dcc856f89a08.png)

![image](https://user-images.githubusercontent.com/64548919/159168825-1c3639a6-04fd-438f-b6ef-74f8ddcb7626.png)

![image](https://user-images.githubusercontent.com/64548919/159168849-c477b9cd-d3bd-4f53-a4ff-0c41dd66c397.png)

We can see the name is `ns1.sina.com.cn`, source ip is `36.51.252.8` and port number is `53`.

There is one answer in the response:

![image](https://user-images.githubusercontent.com/64548919/159168892-722577e8-8fd4-4a1a-bc72-82f74ac71acb.png)

And the value of `AA` is 1:

![image](https://user-images.githubusercontent.com/64548919/159169051-c3d74096-9234-474e-a761-8bbef45bb159.png)

- Try again for the same Query

![image](https://user-images.githubusercontent.com/64548919/159169107-db9e28a0-c65f-4a64-994e-6f2500854c6e.png)

We can see the source ip address is not identical as previous, so they are not the same server.





