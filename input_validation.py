import re

# Exercise 1
# Create a python script that prompts the user to enter their name, age and email adress
# Validate the inputs 

# Check that the name is a non-empty string containing only aplhabetic characters

while True:
    name = input("Name: ").replace(" ", "")
    if name.isalpha():
        break
    else:
        print("invalid name. Please try again")

# Check that age is an integer between 1-120
while True:
    try: 
        age = int(input("Age: "))
        if age < 1 or age > 120:
            raise ValueError
        break
    except ValueError:
        print("Invalid age. Please try again")

# Check that the Email adress is in valid format

email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

while True:
    email = input("Email: ").strip()
    if re.match(email_pattern, email):
        break
    print("Invalid email address. Please enter a valid one.")



print(f"Inputs validated. Name: {name} Age:{age} Email:{email}")