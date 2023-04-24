a = 1
while a<=50:
    if a%5 == 0:
        print(a)
    a += 1


for item in range(51):
    if item%5 == 0:
        print(item)


print(list(range(5,51,5)))

print('''-------------使用continue---------------------''')


for item in range(51):
    if item%5 != 0:
        continue
    print(item)
