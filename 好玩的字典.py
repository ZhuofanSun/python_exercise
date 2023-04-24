class VStore:
    def __init__(self):
        self.store = dict()

    def add(self, value):
        self.store[value]=True

    def delete(self, value):
        if value in self.store:
            del self.store[value]

    def find(self, value):
        if value in self.store:
            return True
        else:
            return False
    def print_all(self):
        print(self.store.keys())

    def __str__(self):
        return "%s" % self.store


x = VStore()
x.add(1)
print(x.find(1))
x.delete(1)
print(x.find(1))
print(x.find(2))
x.print_all()