# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента. '
# 'Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.



class Student:
    def __init__(self, name, surname, age, avg_grade):
        self.name = name
        self.surname = surname
        self.age = age
        self.avg_grade = avg_grade

    def greet(self):
        return f"My name is {self.name}, my surname is {self.surname} and I\'am {self.age} years old"

    def grade(self, new_grade = 77):
         self.avg_grade = new_grade
         return f"New average grade: {new_grade}"

student = Student("Jack", "Dou", 20, 85)

print(student.greet())
print(f"Old average grade: {student.avg_grade}")
print(student.grade())
