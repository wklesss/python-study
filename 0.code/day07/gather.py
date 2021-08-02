# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法（面向对象部分会进行详细讲解）
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)
# 向集合添加元素和从集合删除元素。
set1.add(4)# 增加4
set1.add(5)# 增加5
set2.update([11, 12])# 增加11， 12
set2.discard(5)# 删除5
if 4 in set2:
    set2.remove(4)# 删除4
print(set1, set2)
print(set3.pop())# 提取并打印set3第一项
print(set3)# 打印set3剩余部分
# 集合的成员、交集、并集、差集等运算。
# 集合的成员、交集、并集、差集、对称差运算
print(set1, set2)
print(set1 & set2)# 交集
print(set1 | set2)# 并集
print(set1 - set2)# 差集
print(set1 ^ set2)# 对称差
# 判断子集和超集
print(set2 <= set1)
print(set3 <= set1)
print(set1 >= set2)
print(set1 >= set3)