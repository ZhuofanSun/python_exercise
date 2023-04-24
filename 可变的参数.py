def fun(*args):
    print(args)


fun(1, 2, 3, 34, 5, 6)


def fun1(**args):
    print(args)


X = fun1(a=20, b=30, c=40)


def fun(a, b, c):
    print(a, b, c)


lst = [10, 20, 30]
fun(*lst)  # 在函数调用时，将列表中的每个元素都转换为位置实参传入


def fun5(a=100, b=200, c=300):
    print('a=', a)
    print('b=', b)
    print('c=', c)


x = {'a': 10, 'b': 20, 'c': 30}
fun5(**x)


def asd(a, b=10):
    print('a=', a)
    print('b=', b)


def asd1(*args):#个数可变位置形参
    print(args)


def asd2(**args):#个数可变关键字形参
    print(args)


asd(12, 13)
asd1(11, 22, 33, 44)
asd2(a=11, b=22, c=33)
