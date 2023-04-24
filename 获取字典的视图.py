scores = {'zhangsan': 100, 'lisi': 200, 'wangwu': 300}
keys=scores.keys()
print(keys)
print(type(keys))
lis=list(keys)
print(lis)
for item in lis:
    print(item, end='\n')





value=scores.values()
print(value)
print(type(value))
for item in value:
    print(item, end='  \n')





scores.items()
print(scores)