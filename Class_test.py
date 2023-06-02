class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfun(self):
        print("Hello, my name is "+ self.name)
        print(f" I'm {self.age} years old.")

p1 = Person("John", 28)
p1.myfun()

p1.age = 29
p1.myfun()