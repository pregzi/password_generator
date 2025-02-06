# This is a password generator
import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
           "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f",
           "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "=", "+", "<", ">", "?", "/"]

print("Welcome to the Password Generator")
nr_letters = int(input("How many letters do you want in your password_list? :"))
nr_numbers = int(input("How many numbers do you want in your password_list? :"))
nr_symbols = int(input("How many symbols do you want in your password_list? :"))

# # Easy Method
# password_list = ""
#
# for char in range(0, nr_letters):
#     password_list += random.choice(letters)
#
# for char in range(0, nr_numbers):
#     password_list += random.choice(numbers)
#
# for char in range(0, nr_symbols):
#     password_list += random.choice(symbols)
#
# print(password_list)


# Hard Method
password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)
#print(password_list)

password = ''
for i in password_list:
    password += i
print(password)

