def count_chars(text):
    vowels = 0
    consonants = 0
    spaces = 0
    others = 0

    for char in text:
        if char.lower() in "aeiou":  
            vowels += 1
        elif char.isalpha():  
            consonants += 1
        elif char == " ":  
            spaces += 1
        else:  
            others += 1

    print("Vowels:", vowels)
    print("Consonants:", consonants)
    print("Spaces:", spaces)
    print("Other characters:", others)


text = input("Enter a string: ")
count_chars(text)