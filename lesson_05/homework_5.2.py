# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

#1
one_person = ('Bohdan', 'Zakovorotnyi', 29, 'QA Engineer', 'Sunny Beach')
people_records.insert(0, one_person)
print(f"#1. New record: {people_records}")

#2
element_1 = people_records[1]
element_5 = people_records[5]
people_records.pop(1)
people_records.pop(5)
people_records.insert(1, element_5)
people_records.insert(5, element_1)
print(f"#2. Swapped elements with indexes 1 and 5:{people_records}")

#3
checking_age = (people_records[6][2], people_records[10][2], people_records[13][2])
more_30 = ()
less_30 = ()
for i in checking_age:
    if i >= 30:
        more_30 = more_30 + (i,)
    else:
        less_30 = less_30 + (i,)

if not more_30:
    print(f"#3. No people over 30: {more_30}")
else:
    print(f"#3. Available age over 29: {less_30}")

if not less_30:
    print(f"    No people under 30: {more_30}")
else:
    print(f"    Available age under 30: {less_30}")