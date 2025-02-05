def sum_of_digits(text):
    total = 0

    for char in text:
        if char.isdigit():  # Check if it's a number
            total += int(char)

    print("Sum of digits:", total)

# Get input from the user
text = input("Enter a string with numbers: ")
sum_of_digits(text)