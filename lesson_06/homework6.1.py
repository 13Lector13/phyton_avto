string = input("Enter your string: ")
my_set = set(string)
res = {key: string.count(key) for key in my_set}
print(len(res) > 10)

