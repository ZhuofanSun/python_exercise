sum = 0
num = input('please input a number: ')
print(num)
while num != 'stop':
    sum += float(num)
    print(sum)
    num = input('please input a number: ')
print(sum)