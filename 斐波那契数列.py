# 1  1  2  3  5  8  13
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)#定义这个什么数列的第n位的函数

x=int(input('enter a number: '))
fiblist=[]
for i in range(1, x+1):
    fiblist.append(fib(i))

print(fiblist)#以list输出前n位



