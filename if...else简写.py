#键盘录入两个整数， 比较两个整数的大小
X = int(input('please input an integer'))
Y = int(input('please input another integer'))
if X < Y:
    print(X,'is smaller than',Y)
elif X >= Y:
    print(X,'is greater than or equal to',Y)

print('this is another method')
print(str(X)+' is smaller than '+str(Y)   if X < Y else  str(X)+' is greater than or equal to '+str(Y))