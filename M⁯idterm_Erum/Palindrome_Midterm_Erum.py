def is_palindrome(number):
    return str(number) == str(number)[::-1]  

with open("numbers.txt", "r") as file:
    lines = file.readlines()  

for i, line in enumerate(lines, start=1):
    numbers = [int(num) for num in line.strip().split(',') if num]  
    if not numbers:  
        continue  

    total = sum(numbers)  
    result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
    print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
