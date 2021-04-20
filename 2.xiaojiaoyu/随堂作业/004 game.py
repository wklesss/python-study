import random
secret = random.randint(1,10)
print('..........我爱工作室.......')
temp = input("不妨猜一下我心里想的是那个数字:")
guess = int(temp)
i = 1
while (guess != secret) and (i <= 4) :
    i = i+1
    temp = input("再来一次:")
    guess = int(temp)
    if guess == secret :
        print("好厉害")
        print("猜中也没有奖励的！")
    else:
        if guess > secret:
            print('大了大了')
        else:
            print("这回又小了！")
print("游戏结束")
