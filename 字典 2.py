xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 175,
            "weight": 75.5
            }
print(xiaoming)

print(xiaoming["name"])
xiaoming["age"] = 20
xiaoming["like"] = "小小明"
print(xiaoming)  # 如果key不存在，会新增。如果存在，会更改
xiaoming.pop("like")
print(xiaoming)  # 删除
'''xiaoming.pop("like")
print(xiaoming)
'''  # 删除指令：如果删除的不存在，会报错

print('''---------------------------------------''')
print(len(xiaoming))  # 长度

xiaoming2 = {"height2": 1.75, "height": 200}
xiaoming.update(xiaoming2)
print(xiaoming)
xiaoming.update()  # 向字典里面新增值/又重复的会覆盖
xiaoming.clear()
print(xiaoming)  # 清空
print("----------------遍历--------------------------")
xiaoming={"name": "小明",
            "age": 18,
            "gender": True,
            "height": 175,
            "weight": 75.5}
for k in xiaoming:
    print("%s - %s"%(k,xiaoming[k]))

