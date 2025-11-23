#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
print("task 01 :")
alice_in_wonderland = "\n\"Would you tell me, please, which way I ought to go from here?\"\n\"That depends a good deal on where you want to get to,\" said the Cat.\n\"I don\'t much care where ——\" said Alice.\n\"Then it doesn\'t matter which way you go,\" said the Cat.\n\"—— so long as I get somewhere,\" Alice added as an explanation.\n\"Oh, you\'re sure to do that,\" said the Cat, \"if you only walk long enough.\""
print(f"\nВаріант1: Декілька фізичних ліній: \n {alice_in_wonderland}")
alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""
print(f"\nВаріант2: Декілька фізичних ліній: \n {alice_in_wonderland}")

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("task 02 :")
print(f"Всі символи одинарної лапки (') у тексті:")
for symbol in alice_in_wonderland:
    if symbol == "'":
        print(symbol)
# task 03 == Виведіть змінну alice_in_wonderland на друк
print("task 03 :")
print(alice_in_wonderland)
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
from calendar import month

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
print("\ntask 04 :")
black_see_square = 436402
azov_sea_square = 37800
final_square = black_see_square + azov_sea_square
print(f"\nПлоща Чорного та Азовського моря разом: {final_square}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
print("\ntask 05 :")
three_warehouses = 375291
first_and_second = 250449
second_and_third = 222950
warehouse1 = three_warehouses - second_and_third
warehouse3 = three_warehouses - first_and_second
warehouse2 = three_warehouses - (warehouse1 + warehouse3)
print(f"\n1 склад: {warehouse1} товарів")
print(f"2 склад: {warehouse2} товарів")
print(f"3 склад: {warehouse3} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
print("\ntask 06 :")
number_of_month = 18
amount_per_month = 1179
computer_cost = number_of_month * amount_per_month
print(f"\nВартість комп’ютера: {computer_cost} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
print("\ntask 07 :")
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f"\nОстача від діленя чисел: \n a = {a} \n b = {b} \n c = {c} \n d = {d} \n e = {e} \n f = {f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
print("\ntask 08 :")
big_pizza = 4 * 274
medium_pizza = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
birthday_cost = big_pizza + medium_pizza + juice + cake + water
print(f"\nГрошей знадобиться для дня народження: {big_pizza} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
print("\ntask 09 :")
number_of_photos = 232
number_photos_per_page = 8
number_of_needed_pages = int(-(-number_of_photos // number_photos_per_page))
print(f"\nСторінок знадобиться, щоб вклеїти всі фото: {number_of_needed_pages} ")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
print("\ntask 10 :")
distance_beetwen_two_cities = 1600
fuel_tank_capacity = 48
amount_of_gas_per_100km = 9
needed_gas = (distance_beetwen_two_cities / 100) * amount_of_gas_per_100km
number_of_gas_refills = int(needed_gas // fuel_tank_capacity)
print(f"\nЗнадобиться {needed_gas} літрів бензину для такої подорожі")
print(f"Кількість разів необхідних родині заїхати на заправку під час цієї подорожі: {number_of_gas_refills}")