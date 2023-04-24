
def fun(arg1, arg2):
    print('arg1= ', arg1)
    print('arg2= ', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1= ', arg1)
    print('arg2= ', arg2)


n1 = float(11)
n2 = [22, 33, 44]
print(n1)
print(n2)
fun(n1, n2)  # 按顺序传
print('n1', n1)
print('n2', n2)
