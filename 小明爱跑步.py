class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return 'I am %s,my weight is %.2f kg' % (self.name, self.weight)
    def run(self):
        self.weight-=1.0
    def eat(self):
        self.weight+=0.5
xiaoming = Person('xiaoming',75.0)
xiaomei = Person('xiaomei', 45.0)
xiaoming.eat()
xiaomei.eat()
xiaomei.run()
xiaoming.run()
print(xiaoming)
print(xiaomei)

