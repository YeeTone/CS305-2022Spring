# PA2: Danmaku System

Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Additional Libraries
> from urllib.parse import unquote

## System Design
This system implements a simple version of Danmaku, which supports users to send Danmaku of different font size and color.

This is a simple diagram for this system:

![image](https://user-images.githubusercontent.com/64548919/164993161-27dbe9fe-a9ff-4136-89c2-457d55ce9f88.png)

Overall Effect:

![image](https://user-images.githubusercontent.com/64548919/164993252-0bab9944-73b2-41a7-b77a-7b791e6d48f6.png)

Supporting Functions:
1. Share Danmaku between two clients
2. Support selecting colors, font size of Danmaku
3. Support loading history Danmaku(HTTP version only)


## Running Result

### WebSocket
Open 2 HTML clients of WebSocket programs:

![image](https://user-images.githubusercontent.com/64548919/164993394-be91e906-05a3-4c87-b56f-04dcd727e621.png)

Input the content in the first client:

![image](https://user-images.githubusercontent.com/64548919/164993440-b1d92182-2c89-4b5f-91be-07e77c9efcc8.png)

We can see that in the second client, the danmaku can be viewed as well:

![image](https://user-images.githubusercontent.com/64548919/164993588-aa15dddc-2de7-4629-98a8-f30f8269d02c.png)

### HTTP
Open 2 HTML clients of HTTP programs(127.0.0.1:8765):

![image](https://user-images.githubusercontent.com/64548919/164993559-4fc1c039-7bad-4d73-807e-22bdb63dd5c6.png)

Input the content in the first client:

![image](https://user-images.githubusercontent.com/64548919/164993664-c78f2a3e-2ea3-4043-a82d-78ed0a80762d.png)

We can see that in the second client, the danmaku can be viewed as well:

![image](https://user-images.githubusercontent.com/64548919/164993684-f60e5eed-1609-4c54-8e0c-fa36729ab654.png)

## Analytical Conclusions
1. WebSocket is bidirectional, while HTTP is single-directional. After the data has been sent, the connection of HTTP will be closed while Websocket won't. In one connection, the client and the server can communicate with each other directly in WebSocket, but not in HTTP. HTTP connection only support the client to send data to the server.
2. WebSocket is less easier to cause network traffic in this design. In the implementation, the client will load all the danmaku from the server thus decreases the efficiency of data transmission.
3. Both of them support polling rules so that they could get the new data from the server. But the http version needs to cost more time since in each poll the client needs to build connection with the server. HTTP connection is stateless.
