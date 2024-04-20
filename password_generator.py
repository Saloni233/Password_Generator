import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set(s) for password:
         1. Digits (0-9)
         2. Letters (a-z, A-Z)
         3. Special characters (!@#$%^&*()_-+=<>?/|\{}[]`)
         4. Exit''')

characterList = ""

# Getting character set(s) for password
while True:
    choice = int(input("Pick a number: "))

    if choice == 1:
        characterList += string.digits
    elif choice == 2:
        characterList += string.ascii_letters
    elif choice == 3:
        characterList += string.punctuation
    elif choice == 4:
        break
    else:
        print("Please pick a valid option!")

# Generating random password
password = []
for _ in range(length):
    randomchar = random.choice(characterList)
    password.append(randomchar)

# Printing the generated password as a string
print("The random password is: " + "".join(password))
