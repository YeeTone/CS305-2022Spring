# CS305-2022Spring Lab3 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice 1: Different Status Coded
### Q1-1: Handling More Circumstances of Different Status Code

Source code(Consider using different interfaces to trigger different response and status code):
```python
import socket

ok200 = [b'HTTP/1.0 200 OK\r\n',
         b'Connection: close'
         b'Content-Type:text/html; charset=utf-8\r\n',
         b'\r\n',
         b'<html><body>Hello World!<body></html>\r\n',
         b'\r\n']

noContent204 = [b'HTTP/1.0 204 No Content\r\n',
                b'Connection: close'
                b'Content-Type:text/html; charset=utf-8\r\n',
                b'\r\n',
                b'<html><body>204 No Content<body></html>\r\n',
                b'\r\n']

badRequest400 = [b'HTTP/1.0 400 Bad Request\r\n',
                 b'Connection: close'
                 b'Content-Type:text/html; charset=utf-8\r\n',
                 b'\r\n',
                 b'<html><body>400 Bad Request<body></html>\r\n',
                 b'\r\n']

notFound404 = [b'HTTP/1.0 404 Not Found\r\n',
               b'Connection: close'
               b'Content-Type:text/html; charset=utf-8\r\n',
               b'\r\n',
               b'<html><body>404 Not Found<body></html>\r\n',
               b'\r\n']

intern500 = [b'HTTP/1.0 500 Internal server error\r\n',
             b'Connection: close'
             b'Content-Type:text/html; charset=utf-8\r\n',
             b'\r\n',
             b'<html><body>500 Internal server error<body></html>\r\n',
             b'\r\n']

service503 = [b'HTTP/1.0 503 Service unavailable\r\n',
              b'Connection: close'
              b'Content-Type:text/html; charset=utf-8\r\n',
              b'\r\n',
              b'<html><body>503 Service unavailable<body></html>\r\n',
              b'\r\n']


def web():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(10)
    while True:
        conn, address = sock.accept()
        data = conn.recv(2048).decode().split('\r\n')
        print(data[0])
        print(data[0].split(' '))
        res = notFound404

        s = data[0].split(' ')[1]
        if s == '/':
            res = ok200
        elif s == '/bad-request':
            res = badRequest400
        elif s == '/no-content':
            res = noContent204
        elif s == '/internal':
            res = intern500
        elif s == '/service':
            res = service503

        for line in res:
            conn.send(line)
        conn.close()


if __name__ == "__main__":
    try:
        web()
    except KeyboardInterrupt:
        pass
```

Running Screenshots:
- 200 OK:

![image](https://user-images.githubusercontent.com/64548919/158731396-8f91ae1f-10e2-4d19-927f-a4c9806fa2f3.png)

- 204 No Content:

![image](https://user-images.githubusercontent.com/64548919/158731572-bc7727d0-0a10-43e1-8e27-1369a0f24ac8.png)

- 400 Bad Request:

![image](https://user-images.githubusercontent.com/64548919/158731672-afb89da3-0479-460e-9848-53e35b37d389.png)

- 404 Not Found:

![image](https://user-images.githubusercontent.com/64548919/158731783-f528800c-7ffc-43e1-94ff-aa740cb144a4.png)

- 500 Internal Server Error:

![image](https://user-images.githubusercontent.com/64548919/158731885-410d1014-1325-41ea-943c-2135115706e9.png)

- 503 Service unavailable:

![image](https://user-images.githubusercontent.com/64548919/158731954-b01f4d6e-baee-4a04-a36b-d3db96fbcb72.png)

### Q1-2: Use Wireshark to Capture and Analyze the Packets

- 200 OK:

First run the python script and enable the localhost server：

```
python3 main.py
```

Then open Wireshark and set the display filter:

```
tcp.port == 8080
```

Start capturing packets:

![image](https://user-images.githubusercontent.com/64548919/158733214-5f95908a-1643-471d-ace0-4003f8d71f6b.png)

Send request to the server by typing the following in the command line:
```
curl 127.0.0.1:8080/
```

Now we can get the packets from the Wireshark:

![image](https://user-images.githubusercontent.com/64548919/158733381-99558784-6689-4308-a267-4691bcb42c45.png)

Then we select this packet:

![image](https://user-images.githubusercontent.com/64548919/158734398-d7259ed3-b5d7-49b8-9349-d504edf45972.png)


Soruce IP and Destination IP, Source Port and Destination Port:

![image](https://user-images.githubusercontent.com/64548919/158734206-57db7bb6-b529-4f3d-92b0-c83d397fbb88.png)

Response Status Code:

![image](https://user-images.githubusercontent.com/64548919/158734318-12d51d22-0500-4037-b6f2-526a66a00716.png)

So for the request whose status code is 200 OK, we get the information in the packets using Wireshark:
```
Source IP: 127.0.0.1
Destination IP: 127.0.0.1
Source Port: 8080
Destination Port: 5866
Response Status Code: 200
```

- 204 No Content: 

![204-1](https://user-images.githubusercontent.com/64548919/158736038-ebe854a3-7028-4a94-8b88-a7707323adf5.png)

![204-2](https://user-images.githubusercontent.com/64548919/158736045-07fc3ac7-ee22-4498-8793-2883a06458e3.png)

- 400 Bad Request:

![400-1](https://user-images.githubusercontent.com/64548919/158736091-816a4952-e182-4a0d-b1ce-a3c87bf4980f.png)

![400-2](https://user-images.githubusercontent.com/64548919/158736102-94ec92ec-cd38-4775-840b-e6fb4eec1c60.png)

- 404 Not Found:

![404-1](https://user-images.githubusercontent.com/64548919/158736125-d44d2e5c-73e9-4de7-bdb1-7a0e3c51e60c.png)

![404-2](https://user-images.githubusercontent.com/64548919/158736147-7257480c-1dd7-4028-90b2-87d7e14a666e.png)

- 500 Internal Server Error:

![500-1](https://user-images.githubusercontent.com/64548919/158736187-bcf631a6-85de-450c-86de-55523b4874b6.png)

![500-2](https://user-images.githubusercontent.com/64548919/158736193-ea801a05-6634-4d05-993f-0bdca0d40009.png)

- 503 Service Unavailable:

![503-1](https://user-images.githubusercontent.com/64548919/158736225-bc8383d1-b1ff-4979-aca8-283d8e9c39af.png)

![503-2](https://user-images.githubusercontent.com/64548919/158736234-75e5f40f-197d-4b3b-b372-a74402addd68.png)

These running result can be seen in the following table:

| Type                      | Source IP | Destination IP | Source Port Number | Destination Port Number | Response Status Code |
|---------------------------|-----------|----------------|--------------------|-------------------------|----------------------|
| 200 OK                    | 127.0.0.1 | 127.0.0.1      | 8080               | 5866                    | 200                  |
| 204 No Content            | 127.0.0.1 | 127.0.0.1      | 8080               | 2358                    | 204                  |
| 400 Bad Request           | 127.0.0.1 | 127.0.0.1      | 8080               | 11672                   | 400                  |
| 404 Not Found             | 127.0.0.1 | 127.0.0.1      | 8080               | 11766                   | 404                  |
| 500 Internal Server Error | 127.0.0.1 | 127.0.0.1      | 8080               | 11856                   | 500                  |
| 503 Service unavailable   | 127.0.0.1 | 127.0.0.1      | 8080               | 4823                    | 503                  |
