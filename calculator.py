"""
Just adding this to remind me of the multi-line format
"""

def main():
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    z = divide(x, y)

    print(f"{z:,.2f}")
    print(z)

def divide(x, y):
    return x / y

main()