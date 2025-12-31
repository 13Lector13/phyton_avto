# Завдання 1
#
# Створіть клас Employee, який має атрибути name та salary. Далі створіть два класи, Manager та Developer, які успадковуються від Employee. Клас Manager повинен мати
# додатковий атрибут department, а клас Developer - атрибут programming_language.
#
# Тепер створіть клас TeamLead, який успадковується як від Manager, так і від Developer. Цей клас представляє керівника з команди розробників. Клас TeamLead повинен
# мати всі атрибути як Manager (ім'я, зарплата, відділ), а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.
#
# Напишіть тест, який перевіряє наявність атрибутів з Manager та Developer у класі TeamLead
#

print("Завдання 1")

class Employee:
    def __init__(self, name="", salary=0):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name="", salary=0, department=""):
        super().__init__(name, salary)
        self.department = department

class Developer(Employee):
    def __init__(self, name="", salary=0, programming_language=""):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name="", salary=0, department="", team_size=0):
        super().__init__(name, salary, department)
        self.team_size = team_size

team_lead = TeamLead("Jack", 5000, "IT", 20)
print(team_lead.name)
print(team_lead.salary)
print(team_lead.department)
print(team_lead.team_size)

# Завдання 2
#
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте
# математично вірні для них методи для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

print("\nЗавдання 2")

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod

    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.__side = side

    def perimeter(self):
        return 4 * self.__side

    def area(self):
        return self.__side ** 2

class Rectangle(Shape):

    def __init__(self, a_side, b_side):
        self.__a_side = a_side
        self.__b_side = b_side

    def perimeter(self):
        return 2 * (self.__a_side + self.__b_side)

    def area(self):
        return self.__a_side * self.__b_side

class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def perimeter(self):
        return 2 * pi * self.__radius

    def area(self):
        return pi * self.__radius ** 2

square = Square(5)
rectangle = Rectangle(4, 8)
circle = Circle(3)

print(square.perimeter())
print(square.area())
print(rectangle.perimeter())
print(rectangle.area())
print(circle.perimeter())
print(circle.area())