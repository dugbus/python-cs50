"""
First Python script
This is a simple Python script that prints "Hello, Name!" to the console.
"""

# Ask User for their name
name = input("What is your name? ")

#Remove any leading or trailing whitespace and capitalize
name = name.strip().title()

# Check if the name is empty
if not name:
    print("You didn't enter a name!")
else:
    print(f"Hello, {name}!")
