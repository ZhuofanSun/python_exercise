lst = input().split()
count = {}
for num in lst:
    if num in count:
        count[num]+=1
    else:
        count[num]=1
lst1 = []
for i in count:
    lst1.append(count[i])
print(max(lst1))
