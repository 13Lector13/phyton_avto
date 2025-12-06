my_list = list(input("Enter a string with numbers: "))

numbers_list = []
for i in my_list:
    if i.isdigit():
        numbers_list.append(int(i))

even_numbers = [x for x in numbers_list if x % 2 == 0]
print(even_numbers)

even_numbers_sum = sum(even_numbers)
print(even_numbers_sum)