# PA1: DNS Server Implementation

Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

You can follow these steps to test the function of LocalDNSServer.

## Network Information
Use`ipconfig`to get the ip addresss of my computer:

![image](https://user-images.githubusercontent.com/64548919/160831590-d1d19e1b-5a08-4a89-8868-bb8fde280f47.png)

We can get the ip address is `10.26.128.169`

## Execute `LocalDNSServer.py`
Type the following in the directory of `LocalDNSServer.py`
```
python3 LocalDNSServer.py
```

and input these in the command line:

```
10.26.128.169
55
```

Like this:

![image](https://user-images.githubusercontent.com/64548919/160832457-ac0f3210-ba07-4e3c-8ea0-f64092cdaf97.png)

## Tests on the document

### www.baidu.com
Open another terminal, and type this in the command line:

```
dig @127.0.0.1 www.baidu.com a -p 5533
```

And here is the result.

![image](https://user-images.githubusercontent.com/64548919/160832810-366460ac-f93d-46a1-a778-f48b1952d4ce.png)

**Notice that there may be a bug that in the answer section, the CNAME field is not added into the result. (I tried my best to fix it, but did not succeed)**

### www.sina.com
Continue using the terminal in the previous section and type:

```
dig @127.0.0.1 www.sina.com a -p 5533
```

![image](https://user-images.githubusercontent.com/64548919/160833337-4796c863-b453-4888-9bfa-b2f08847e5a4.png)

### www.sustech.edu.cn
Continue using the terminal in the previous section and type:

```
dig @127.0.0.1 www.sustech.edu.cn a -p 5533
```

![image](https://user-images.githubusercontent.com/64548919/160833563-7343c576-1728-4bad-8516-f5a1266fb1d5.png)

### www.bilibili.com
Continue using the terminal in the previous section and type:

```
dig @127.0.0.1 www.bilibili.com a -p 5533
```

![image](https://user-images.githubusercontent.com/64548919/160833774-a406db42-72de-4abc-b403-972484a6d14f.png)

### www.github.com
Continue using the terminal in the previous section and type:

```
dig @127.0.0.1 www.github.com a -p 5533
```

![image](https://user-images.githubusercontent.com/64548919/160833891-80025b05-e74c-4692-81c4-d150c01c089e.png)

### www.baidu.com again(Read cache)
Continue using the terminal in the previous section and type:

```
dig @127.0.0.1 www.baidu.com a -p 5533
```

![image](https://user-images.githubusercontent.com/64548919/160834609-8a89e632-771f-4535-9193-a1b5dca03cfc.png)

Please notice that when reading cacahe, the CNAME type can be displayed correctly.

And here is the result in the terminal of `LocalDNSServer.py`:

![image](https://user-images.githubusercontent.com/64548919/160834811-030903e6-3e9a-4de3-8560-ea4617ddad71.png)

### www.baidu114514.com (a domain name cannot be queried)

Continue using the terminal in the previous section and type:

```
dig @127.0.0.1 www.baidu114514.com a -p 5533
```

![image](https://user-images.githubusercontent.com/64548919/160837903-e3b698a1-e791-47a8-9e57-f571696516c5.png)

![image](https://user-images.githubusercontent.com/64548919/160837939-89cd47de-ad5d-43e0-b0f7-71d5cddf30be.png)


