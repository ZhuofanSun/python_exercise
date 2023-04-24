scores = {'zhangsan': 100, 'lisi': 90, 'wangwu': 45}
print(scores['zhangsan'])  # 第一种方式，使用【】
print(scores.get('zhangsan'))  # 第二种方式，get（）
# print(scores['chenliu'])     报错
print(scores.get('chenliu'))  # 不会报错
print(scores.get('chenliu', 99))  #查找的键不存在时的默认值

