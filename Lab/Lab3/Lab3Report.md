# CS305-2022Spring Lab3 Report
Name：Yitong WANG 11910104@mail.sustech.edu.cn

Student ID：11910104

Lab Time：Thursday 10:20 a.m. to 12:10 p.m.

Lab Teacher：Qing WANG wangq9@mail.sustech.edu.cn

Lab SA:
- Siyu LIU 11912935@mail.sustech.edu.cn
- Xingying ZHENG 11912039@mail.sustech.edu.cn

## Practise 1: MIME Types of Files

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
