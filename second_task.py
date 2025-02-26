from abc import ABC

print('TASK_1')
for el1 in range(1, 11):
    print(el1, end=' ')

print('')
for el2 in range(1, 21):
    if el2 % 2 == 0:
     print(el2, end=' ')

print('')
for el3 in range(10, 0, -1):
    print(el3, end=' ')

print('')
print('TASK_2')
for m1 in range(1, 11):
    res = m1 * 10
    print(f' 10 * {m1} = {res}')

print('')
print('TASK_3')
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f'Привіт, мене звуть {self.name}'

class Student(Person):
    def __init__(self, name, is_student = True):
        Person.__init__(self, name)
        self.student = is_student

    def is_student(self):
        return self.student

student = Student('Аліна')

print(student.greet())
print(student.is_student())

print('')
print('TASK_4')
class Shape(ABC):
    def __init__(self, area):
        self.area = area

class Circle(Shape):
    def __init__(self, area, radius):
        super().__init__(area)
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, area, width, height):
        super().__init__(area)
        self.width = width
        self.height = height