import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#The program will ask:

#How many letters would you like in your password?
#How many symbols would you like?
#How many numbers would you like?
#The objective is to take the inputs from the user to these questions and then generate a random password.

print("Welcome to my Python Password Generator!")
pw_letters = int(input("How many letters would you like in your password?\n"))
pw_symbols = int(input(f"How many symbols would you like?\n"))
pw_numbers = int(input(f"How many numbers would you like?\n"))

# Dynamic password generation
password_list = []
for char in range(0, pw_letters):
    password_list.append(random.choice(letters))

for char in range(0, pw_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, pw_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

