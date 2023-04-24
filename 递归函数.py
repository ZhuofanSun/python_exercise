x=int(input('please input a number: '))
jiecheng=1
for i in range(1,x+1):
    jiecheng=i*jiecheng
print(jiecheng)

print('--------------------------递归函数（阶乘）-------------------------')
def fac(n):
    if n == 1:
        return 1
    else:
        return  n*fac(n-1)
print(fac(3))