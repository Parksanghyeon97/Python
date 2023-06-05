from Person import Person

class Student(Person):
    def study(self):
        print('열공열공...')

lee = Person()
print(lee.mouth)
lee.talk()

kim = Student()
print(kim.mouth)
kim.talk()
kim.study()