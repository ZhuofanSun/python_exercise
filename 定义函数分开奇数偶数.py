def fun(num):
    odd = []
    even = []
    for i in num:
        if i % 2 == 0:
            odd.append(i)
        else:
            even.append(i)
    return even, odd


lst = [14, 14, 15, 14, 5, 34, 7, 5478, 23, 6, 26, 467, 123]
print(fun(lst))
