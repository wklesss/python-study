# 创建字典的字面量语法
scores ={'wk':22, 'kk':23, 'ww':24}
print(scores)
# 创建字典的构造器语法
items1 = dict(one=1, two=2, three=3, four=4)
# 通过zip函数将两个序列压成字典
items2= dict(zip(['a', 'b', 'c'], '123'))
# 创建字典的推导式语法
items3 = {num: num ** 2 for num in range(1, 10)}
print(items1, items2, items3)
# 通过键可以获取字典中对应的值
print(scores['wk'])
print(scores['kk'])
# 对字典中所有键值进行遍历
for key in scores:
    print(f'{key}: {scores[key]}')
 # 更新字典中的元素
scores['kk'] = 33
scores['ww'] = 44
scores.update(www=55, kkk=66)
print(scores)
if 'kk' in scores:
    print(scores['kk'])
print(scores.get('kk'))
# get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('kk', 55))
# 删除字典中的元素
print(scores.popitem())
print(scores.popitem())
print(scores.pop('kk', 100))
# 清空字典
scores.clear()
print(scores)