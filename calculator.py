def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", add(a, b))
    print("Difference:", subtract(a, b))

if __name__ == "__main__":
    main()