"""
First Python script
This is a simple Python script that prints "Hello, Name!" to the console.
"""

def main():
    # Ask User for their name
    name = input("What is your name? ")

    #Remove any leading or trailing whitespace and capitalize
    name = name.strip().title()

    greet(name)

    greet()

# Setting name to world only gives it a default value of world if the function is called without an argument
# It won't set name to world if the function is called with an argument even if that arguement is empty
def greet(name="World"):
    if not name:
        print("You didn't enter a name!")
    else:
        print(f"Hello, {name}!")

main()