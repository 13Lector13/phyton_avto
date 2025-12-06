string = ""
while 'h' not in string:
    string = input("Enter your string with h/H: ")
    if 'h' not in string.lower():
        continue
    else:
        print("Finished")
        break

