"""import sys

#捕获异常： try
try:
    num = int(input("please input an integer: "))
#尝试执行的代码
except:
    print("please input the correct integer")
#出现错误的处理
print("-----"*30)"""
# 提示用户输入一个整数
try:
    num = int(input("pleaase input an integer: "))
    result = 8/num
    print(result)

# 使用8 初一用户输入的整数并且输出
except ZeroDivisionError:
    print("zero division error")
#捕获未知错误
except Exception as result:
    print("unknown error %s"% result)
else:
    print("successfully tried")
finally:
    print("finished")
print("-"*50)
