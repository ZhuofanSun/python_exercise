for i in range(1, 10):
    for j in range(1, i + 1):  # 第i行有i个
        print(i, '*', j, '=', i * j, end='\t')
    print('', end='\n')
