class Animal():
    def __init__(self):
        pass

    def eat(self):
        print("eat")

    def run(self):
        print("run")

    def sleep(self):
        print("sleep")


class Dog(Animal):
    def bark(self):
        print("wangwang")


class Xiaotian(Dog):
    def fly(self):
        print("fly")

    def bark(self):
        print("wo shi shabi")  # 继承的覆盖
        super().bark()
        print("^%^%*^&&$%^%*")


wangcai = Dog()
wangcai.bark()
wangcai.run()
print('-'*50)
dawangcai = Xiaotian()
dawangcai.bark()

wangcai.bark()
