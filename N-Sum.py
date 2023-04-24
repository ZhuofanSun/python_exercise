n, m = input().split()
n = int(n)
m = int(m)
num = []
for i in range(1, n + 1):
    num.append(i)
num.sort(reverse=True)
sum = 0
add_lst = []
for i in num:
    if sum == m:
        break
    elif sum <= m and sum + i <= m:
        sum += i
        add_lst.append(i)
add_lst.sort()
print(len(add_lst))
for i in add_lst:
    print(i, end=' ')
