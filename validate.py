password = input("Enter password: ")

special = ['!', '@', '#', '$', '%', '&', '*']

min_num = 0
char = 0

while len(password) >= 7:
    for i in password:
        if i.isdigit():
            min_num += 1
        if i in special:
            char += 1
    break
if min_num >= 2 and char >= 2:
    print("Strong".strip())
else:
    print("Weak".strip())
