# CS305-2022Spring Lab5 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice5-1: Query using ```dig```
### Step 1: Type the following in the command line:

```
dig www.sina.com.cn +trace
```

This is the screenshot of the output in the command line:

![image](https://user-images.githubusercontent.com/64548919/159166750-34755f96-4ccd-47b5-ad8f-06819128253d.png)

### Step 2: Packet Analysis

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

- Try again for the Same Query

![image](https://user-images.githubusercontent.com/64548919/159169107-db9e28a0-c65f-4a64-994e-6f2500854c6e.png)

We can see the source ip address is not identical as previous, so they are different servers.

This can bring benefits for providing diverted ip address accessing.

## Practice5-2: EDNS Query
### Step 1: Send Query
Type the following in the command line:

```
dig www.bilibili.com +edns
```

Here are the running result in the command line:

![image](https://user-images.githubusercontent.com/64548919/159170459-4abd9af8-3ec9-4226-bb4c-d1f24b438dc8.png)

### Step 2：Analyze the Packets

#### Query Message
- Destination IP Address and Port

![image](https://user-images.githubusercontent.com/64548919/159170515-1f3f0eb7-792c-48d5-a699-e02ecb0f5194.png)

Destination IP Address is `172.18.1.92` and Port is `53`.

- Name, Type and Class

![image](https://user-images.githubusercontent.com/64548919/159170571-e0922a6b-1771-4a45-884a-392c427c2113.png)

Name is `www.bilibili.com`, Type is `A (Host Address)` and Class is `IN (0x0001)`.

- Opcode

![image](https://user-images.githubusercontent.com/64548919/159170634-c76b130b-6295-4d3d-9ce8-630d1820f3e2.png)

The opcode is `0000`, indicating it is a standard query.

- Additional RRs

![image](https://user-images.githubusercontent.com/64548919/159170686-a0b8ee48-20d2-45ce-bd8a-7e8cf1d41528.png)

There is no additional RRs.

#### Response Message

- Answers and TTLs

There are multiple answers, and their TTLs are shown in the following screenshots.

![image](https://user-images.githubusercontent.com/64548919/159170788-44495f1a-cb3a-4d95-9f53-9af8754ce443.png)

- Authority RRs

![image](https://user-images.githubusercontent.com/64548919/159170898-6af31f92-a572-4c25-abfd-8d33a80bee84.png)

There are 2 authority RRs. Their type is `NS (authoritative Name Server) (2)`.

## Practice5-3: DNS Client Implementation
Source code:
```python
import dns.resolver
import sys

domain = sys.argv[1]
queryType = sys.argv[2]

try:
    q = dns.resolver.resolve(qname=domain, rdtype=queryType, raise_on_no_answer=False)
    # print(q.rrset)
    # print(q.qname)
    # print(q.rdtype)
    # print(q.rdclass)
    print('Answer:',q.response)
    print()
    print('Who send the server?',q.nameserver)
    print()
    print('Port Number?', q.port)
    print()
    print('Is from authority name server?','AUTHORITY' in str(q.response))
    #print(q.port)
    #print(q.canonical_name)
except dns.resolver.NoAnswer as na:
    print('This request contains no content')
```

And the following screenshots shows the running results with different parameters:

- www.sina.com.cn A

![image](https://user-images.githubusercontent.com/64548919/159286644-9d90fe89-6657-4dfb-afb1-211f41072825.png)

- www.sina.com.cn AAAA

![image](https://user-images.githubusercontent.com/64548919/159287008-deddf12a-689f-42d1-bb13-944bc02e821f.png)

- www.sina.com.cn CNAME

![image](https://user-images.githubusercontent.com/64548919/159287130-2fa10cb2-9bb4-4567-a5ed-c9ed2bdcd632.png)

- www.sina.com.cn NS

![image](https://user-images.githubusercontent.com/64548919/159287255-2f125a32-018b-4850-b869-2db7fbd0e8dc.png)


- www.sina.com.cn MX

![image](https://user-images.githubusercontent.com/64548919/159287308-48e14155-7558-46bd-8cab-007d4d0edb5e.png)
