class Cat:
    def eat(self):
        print('%s 爱吃鱼' % self.name)

    def drink(self):
        print("%s要喝水" % self.name)


"""创建'猫'对象"""
tom = Cat()

tom.name = "Tom"
tom.drink()
tom.eat()

print('-' * 50)

"""打印地址"""
print(tom)
addr = id(tom)
print("%x" % addr)

print("-" * 50)

"""再创建一个猫对象"""
"""分配了同一处内存"""
lazy_cat = Cat()
lazy_cat.name = '大懒猫'
lazy_cat.eat()
lazy_cat.drink()
print(tom)
print(lazy_cat)
lazy_cat2 = lazy_cat
print(lazy_cat2)

print("-" * 50)

"""可以使用'.'加上属性名  利用赋值语句就可以了"""

print(tom)

print(tom)

tom.eat()
lazy_cat.eat()
