import random

# Character lists
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','(',')']

print("🎉 WELCOME TO PASSWORD GENERATOR! 🎉")

# User input
n_letters = int(input("How many letters do you want in your password?\n"))
n_numbers = int(input("How many numbers do you want in your password?\n"))
n_symbols = int(input("How many symbols do you want in your password?\n"))

# Collect characters in a list
password_list = []

for i in range(n_letters):
    password_list.append(random.choice(letters))

for i in range(n_numbers):
    password_list.append(random.choice(numbers))

for i in range(n_symbols):
    password_list.append(random.choice(symbols))

# Shuffle the characters
random.shuffle(password_list)

# Convert to string
password = ''.join(password_list)

# Output
print("\n✅ Your Generated Password is:\n", password)
