"""
判断一个正整数是不是素数

Version： 0.1
Author： 王凯
Date: 2021-07-29
"""
from math import sqrt, trunc

num = int(input('请输入一个正整数： '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime =False
        break
    if is_prime and num != 1:
        print('%d是素数' % num)
    else:
        print('%d不是素数' % num)