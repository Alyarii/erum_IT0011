def is_palindrome(number):
    return str(number) == str(number)[::-1]  

with open("numbers.txt", "r") as file:
    lines = file.readlines()  

for i, line in enumerate(lines, start=1):
    numbers = list(map(int, line.strip().split(',')))  
    total = sum(numbers)  

    if is_palindrome(total):
        result = "Palindrome"
    else:
        result = "Not a palindrome"

    print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")