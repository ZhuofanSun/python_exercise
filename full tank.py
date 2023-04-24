l, c, n, t = input().split()
l = int(l)
c = int(c)
n = int(n)
t = int(t)
x = input().split()
a = 0
length = 0
length = int(length)
for i in range(len(x)):
    if int(x[i])>(length + c):
        a +=1
        length = int(x[i-1])
if l > (length + c):
    a += 1
time = l + t * a
print(time)


