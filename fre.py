import sys

file = open(sys.argv[1])
txt = file.read()
file.close()
words = txt.split()
x = 0
y = 0
for word in words:
    y += 1
    if word == 'so' or word == 'So':
        x += 1

print('这个傻逼说了 ', x, ' 次so！！！！！！！！！！！！！！！')
print("一共说了", y, '个词！！！！！！！')
