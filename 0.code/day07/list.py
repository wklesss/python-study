import sys
ly1 = ('*' *80)
list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]
list2 = ['hello'] * 3
print(list2)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[-1])
print(list1[-3])
list1[2] =300
print(list1)
for index in range(len(list1)):
    print(list1[index])

for elem in list1:
    print(elem)
    
for index, elem in enumerate(list1):
    print(index, elem)
    
# 添加元素
list1.append(200)
list1.insert(1, 400)
list1 += [1000, 2000]
print(list1)
print(len(list1))

if 3 in list1:
    list1.remove(3)
if 1234 in list1:
    list.remove(1234)
print(list1)
list1.pop(0)
list1.pop(len(list1) - 1)
print(list1)

list1.clear()
print(list1)

# 切片操作
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
fruits2 = fruits[1:4]
print(fruits2)
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]
print(fruits4)
fruits5 = fruits[::-1]
print(fruits5)

# 列表的排序
list3 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list4 = sorted(list1)
list5 = sorted(list3, reverse=True)
list6 = sorted(list3, key=len)
print(list3)
print(list4)
print(list5)
print(list6)
list3.sort(reverse=True)
print(list3)

print(ly1) 

#生成式和生成器
f1 = [x for x in range(1, 10)]
print(f1)
f2 = [x + y for x in 'ABCDE' for y in '1234567']
print(f2)
f3 = [x ** 2 for x in range(1, 1000)]
print(sys.getsizeof(f3))
print(f3)
f4 = (x ** 2 for x in range(1, 1000))
print(sys.getsizeof(f4))
print(f4)
for val in f4:
    print(val)
