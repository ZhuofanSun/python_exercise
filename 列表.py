lst = ['hello', 'world', 98, 'hello']
print(lst[1])
print(lst[0])
print(lst[2])
print(lst.index('hello'))  # 这里是句号
print(lst.index('hello', 1, 4))  # 从第一到第三找hello
lst2 = ['hello', 'world', 98, 'hello', 'what', 234]
print(lst2[2:5:1])
print(lst2[2:5])
print(lst2[2::1])
print(lst2[::-1])
print(lst2[::1], end='*')
print(100 in lst2)
for item in list(lst2):
    print(item, end='  ')
print()
print('''----------------向列表末尾添加一个元素-------------------''')
lst3 = [10, 11, 12, 13, 14, 15, 16]
print(lst3)
print(id(lst3))
lst3.append(29)
print(lst3)
print(id(lst3))
print('''------------------向列表末尾添加多余一个元素--------------------''')
lst3.extend(lst)
print(lst3)
print('''----------------向列表任意一个位置添加一个元素------------------''')
lst3.insert(0, 100)
print(lst3)
print('''----------------向列表任意一个位置添加多个元素------------------''')
lst3[1:] = lst
print(lst3)
print('''-------------------从列表中移走某个元素----------------------''')
lst3.remove(100)
print(lst3)
print('''--------------------根据索引移出元素-------------------------''')
print(lst3)
lst3.pop(0)
print(lst3)
print("-----------------------删除空列表----------------------------")
lst3[1:2] = []
print(lst3)
print("-----------------------清除列表中的所有元素---------------------")
lst3.clear()
print(lst3)
print(3 in [1, 2, 3, 4, 5, 6])
print('---------------------列表的排序操作-----------------------------')
lst4 = [20, 50, 10, 40, 60, 30]
print('original list: ', lst4)
lst4.sort()
print('list after sort: ', lst4)  # 默认正序排列
lst4.sort(reverse=True)
print('list after reverse sort: ', lst4)  # 倒序排列
lst4.sort(reverse=False)
print('lsit after sort: ', lst4)  # 正序排列
print('--------------------------使用内置函数sorted（）对列表进行排序，将产生一个新的列表对象----------------')
lst4 = [20, 50, 10, 40, 60, 30]
print('original list: ', lst4)
newlist = sorted(lst4)
print('排序过的列表', newlist)
newlist1 = sorted(lst4, reverse=True)
print(newlist1)
print('-------------------------列表生成式子--------------------------')
lst5 = [i for i in range(1, 10)]
print(lst5)
lst5.reverse()
print(lst5)

