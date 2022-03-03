# CS305-2022Spring Lab3 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practice 1: MIME Types of Files

- Source code
```python
import mimetypes as mt
import os

path = 'D:\PycharmProjects\mathContest'

allFiles = os.listdir(path)

print('%-25s %-25s'%('File Name', 'MIME Type'))

for f in allFiles:
    print('%-25s %-25s'%(f, mt.guess_type(f)[0]))
```

- Commands and Screenshots

Type this in the command line under the directory of 'D:\PycharmProjects\mathContest':
```
ls
```
Then we can see all the files in the directory.

![image](https://user-images.githubusercontent.com/64548919/156592718-810de068-c202-47e5-9769-4399b8f321a6.png)

Then type this in another command line under the directory of mime.py.

```
python3 mime.py
```

And the MIME types of these files are listed in the running result.

![image](https://user-images.githubusercontent.com/64548919/156593104-2d76e6fb-fe9b-4d4d-8cb9-617d505cab64.png)

## Practice 2: URL & HTTP Response
In this practice, I used ```curl``` to get the status code and the port number of the server.

### Q1 Status code

Type these commands in the command line one by one, and we can get the status codes of these websites.
```
curl http://www.sustech.edu.cn --HEAD -v
curl https://www.sustech.edu.cn --HEAD -v
curl http://sustech.edu.cn --HEAD -v
curl https://sustech.edu.cn --HEAD -v
```

And the status codes are:
```
301
200
301
200
```

![image](https://user-images.githubusercontent.com/64548919/156601760-3e92c87d-37ce-4cdb-a077-147b0b6b66cb.png)

![image](https://user-images.githubusercontent.com/64548919/156601888-c0f77d47-a833-4fca-b2f6-05ea3b3c0bad.png)

![image](https://user-images.githubusercontent.com/64548919/156602126-1ecefca0-faca-4cd9-a605-2b4b995d962e.png)

![image](https://user-images.githubusercontent.com/64548919/156602193-99b1249e-21b1-40d0-8502-4ed6ab61554b.png)


Explain the meaning of status codes:
- 301: Moved and Redirected Permanently
- 200: Request Successfully

### Q2 Server Port Number
Also type the commands in **Q1**, and we can get the server port numbers from the screenshots:

```
80
443
80
443
```
