# This is a Python script to calculate the factorial of a number

def factorial(n):
    """Calculate the factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    """Main function to get user input and print the factorial"""
    num = int(input("Enter a number: "))
    fact = factorial(num)
    print("Factorial of", num, "is", fact)

if __name__ == "__main__":
    main()
