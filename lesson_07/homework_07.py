# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def numbers_sum():
    a = int(input("\ntask 2:\nEnter any integer a: "))
    b = int(input("Enter any integer b: "))
    print(f"Sun of two integers: {a + b}")

numbers_sum()

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def avg_func():
    my_list = list(input("\ntask 3: \nEnter list of numbers: "))
    my_list_int = [int(i) for i in my_list if i.isdigit()]
    avg =[sum((my_list_int)) / len(my_list_int)]
    print(f"Arithmetic mean of a list of numbers: {avg}")

avg_func()


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string():
    my_string = input("\ntask 4: \nEnter any elements: ")
    print(my_string[::-1])

string()


# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word():
    my_string = input("\ntask 5: \nEnter list of any words and separate it with \" \": ")
    my_list = my_string.split(' ')
    sorted_my_list = sorted(my_list, key = lambda x: len(x))
    print(sorted_my_list[-1])
longest_word()


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)
print("task 6:")
str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


# task 7

def func_set():
    string = input("\ntask 7: \nEnter your string: ")
    my_set = set(string)
    res = {key: string.count(key) for key in my_set}
    print(len(res) > 10)
func_set()


# task 8
def h_func():
    string = ""
    while 'h' not in string:
        string = input("\ntask 8: \nEnter your string with h/H: ")
        if 'h' not in string.lower():
            continue
        else:
            print("Finished")
            break
h_func()

# task 9
def str_lst():
    lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
    lst2 = []
    for i in lst1:
        if type(i) == str:
            lst2.append(i)
    print(f"\ntask 9:\n{lst2}")
str_lst()


# task 10
def numbers_sum():
    my_list = list(input("\ntask 10: \nEnter numbers: "))

    numbers_list = []
    for i in my_list:
        if i.isdigit():
            numbers_list.append(int(i))

    even_numbers = [x for x in numbers_list if x % 2 == 0]
    print(even_numbers)

    even_numbers_sum = sum(even_numbers)
    print(even_numbers_sum)
numbers_sum()
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""