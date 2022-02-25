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
