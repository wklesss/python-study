"""
猜数字游戏

Version: 0.1
Author: 王凯
"""
import random
from typing import Counter

answer = random.randint(1,100)
Counter = 0
while True:
    Counter += 1
    number = int(input('请输入： '))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了！')
        break
print('您总共猜了%d次' % Counter)
if Counter > 7:
    print('次数太多，继续加油')