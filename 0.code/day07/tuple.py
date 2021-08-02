# 使用元组
# 定义元祖
t = ('wk', 26, True, 'beijing')
print(t)
# 获取元组中元素
print(t[0])
print(t[3])
# 遍历元组中的值
for member in t:
    print(member)
# 重新给元组赋值
t = ('kk', 22, True, 'shanghai')
print(t)
# 将元组转换成列表
person = list(t)
print(person)
person[0] = 'ww'
person[1] = 24
print(person)
# 将列表转换成元组
fruits_list = ['apple', 'bannan', 'roange']
print(fruits_list)
fruits_tuple =tuple(fruits_list)
print(fruits_tuple)