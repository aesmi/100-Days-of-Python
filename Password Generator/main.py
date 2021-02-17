import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Prompt for user input
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Password array
password = []
passwordList = []

# Randomly select an ASCII char from our num array and push into our password array
for x in range (0, nr_letters):
      random_value = random.randint(0, len(letters))
  password.append(letters[random_value - 1])

for y in range (0, nr_symbols):
  random_value = random.randint(0, len(symbols))
  password.append(letters[random_value - 1])

for z in range (0, nr_numbers):
  random_value = random.randint(0, len(numbers))
  password.append(letters[random_value - 1])

for char in password:
    random.shuffle(passwordList)

print(passwordList)
