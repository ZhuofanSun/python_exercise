"""想从n个礼物中选k个包在一起，有多少种方式"""
#solution1:
import math
n = int(input("n = "))
k = int(input("k = "))
x = int(math.factorial(n)/math.factorial(k)*math.factorial(n-k))
print(x)
#solution2:
count = 0
for i in range(n):
    for j in range(i+1,n):
        count += n-1-j
print(count)