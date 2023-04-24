info_tuple = ("zhangsan", 18, 1.75)
print(info_tuple)
print(type(info_tuple))
print("---------------------------------------------")
a = info_tuple[0]
print(a)  # 索引

empty_tuple = ()
print(empty_tuple, type(empty_tuple))
single_tuple = (5)
print(type(single_tuple))  # int类型（元组里只有一个元素，类型就和这个元素一样
single_tuple = (5,)
print(single_tuple, type(single_tuple))
print("-------------------------元组常用操作--------------------------")
info = ("zhangsan", 18, 1.85,"zhangsan")
print(info[0])
print(info.index("zhangsan"))  # 索引

print(info.count("zhangsan"))
print(len(info))
print("----------------------------遍历-----------------------")
for my_info in info:
    print(my_info,end='  ')
