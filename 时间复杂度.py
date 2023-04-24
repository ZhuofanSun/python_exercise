# # 如果 a+b+c=1000，而且a^2+b^2=c^2（a，b，c为自然数），如何求出所有a，b，c可能的组合？
# import time
# start = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
#                 print(a, b, c)
# end = time.time()
# print(end - start)
# print()

import time

start = time.time()

for a in range(1000):
    for b in range(1000):
        if a ** 2 + b ** 2 == (1000 - a - b) ** 2:
            print(a, b, 1000 - a - b)

end = time.time()
print(end - start)
"""
每台机器执行的总时间不同
但是执行基本运算数量大体相同
所以时间复杂度用运算数量衡量
"""