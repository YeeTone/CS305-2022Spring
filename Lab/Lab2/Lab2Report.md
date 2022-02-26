# CS305-2022Spring Lab2 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice 1
- **Problem: Find Narcissistic Numbers**

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

## Practice 2
- **Problem: Wireshark**

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
