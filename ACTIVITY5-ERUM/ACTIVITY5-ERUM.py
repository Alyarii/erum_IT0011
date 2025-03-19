def divide(a, b):
    if b == 0:
        return "Invalid input. Cannot divide by zero."
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return "Invalid input. Cannot divide by zero."
    return a % b

def summation(a, b):
    if a > b:
        return "Invalid input. Second number must be larger than the first number."
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting program. Goodbye!")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                
                if choice == 'D':
                    result = divide(a, b)
                elif choice == 'E':
                    result = exponentiation(a, b)
                elif choice == 'R':
                    result = remainder(a, b)
                elif choice == 'F':
                    result = summation(a, b)
                
                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter integers only.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
