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

- **Screenshots**

And this is the screenshot of the python source code.
![image](https://user-images.githubusercontent.com/64548919/155740310-37b2a345-b4dd-4a2b-a369-7228fb7897e3.png)
