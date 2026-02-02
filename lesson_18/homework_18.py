# Генератори:
#
# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
n = 99
gen_even = (x for x in range(0, n) if x % 2 == 0)
for i in gen_even:
    print(i)
print("\n")


def fibonacci(f):
    a = 0
    b = 1
    for _ in range(f):
        yield a
        a, b = b, a + b


for fib in fibonacci(10):
    print(fib)
print("\n")

# Ітератори:
#
# Реалізуйте ітератор для зворотного виведення елементів списку.
# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

my_list = [1, "s", "hello", True, 12, 13, "@", False, 0]

for i in iter(my_list[::-1]):
    print(i)
print("\n")


class MyIterator:
    def __init__(self, a):
        self.a = a
        self.current = 0

    def __next__(self):
        if self.current >self.a:
            raise StopIteration()
        value = self.current
        self.current += 2
        return value

    def __iter__(self):
        return self

for x in MyIterator(99):
    print(x)
print("\n")

# Декоратори:
#
# Напишіть декоратор, який логує аргументи та результати викликаної функції.
# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper


@logger
def longest_word(text):
    words = text.split(' ')
    sorted_my_list = sorted(words, key=lambda x: len(x))
    return sorted_my_list[-1]

print(longest_word("5 write ! And do this 13 @ Hello! yes"))



def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] {func.__name__}: {e}")
            return None
    return wrapper

@exception_handler
def avg_func(avg_list):
    my_list_int = []
    for i in avg_list:
        if isinstance(i, int) or isinstance(i, float):
            my_list_int.append(i)
        elif isinstance(i, str) and i.isdigit():
            my_list_int.append(int(i))
    if not my_list_int:
        raise ValueError("No valid numbers entered.")
    avg = sum(my_list_int) / len(my_list_int)
    return avg

print(avg_func([1, "@1", 3, "4", 5, "Hello", 7, True, " ", 10]))
print(avg_func(["@1a", "abc", "!", "Hello", True, " ", False]))
print(avg_func(["Hello", "@", "!"]))
print(avg_func([None, {}, []]))
