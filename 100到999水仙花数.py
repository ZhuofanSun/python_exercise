#水仙花数    例如  153         1**3+5**3+3**3=153

for item in range(100,1000):
    a = item // 100
    b = item // 10 % 10
    c = item % 10
    if a**3+b**3+c**3 == item:
      print(item)