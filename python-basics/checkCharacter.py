# Check if a character is a vowel, consonant, digit, or special character.

ch = input("Enter one character: ")

if len(ch) != 1:
    print("Enter exactly one character")
elif ch.isalpha():
    print("Vowel" if ch.lower() in "aeiou" else "Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character") 
    
    