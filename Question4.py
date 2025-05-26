import string

def case(char):
    if char in string.ascii_uppercase:
        return (f"{char} is an uppercase letter")
    elif char in string.ascii_lowercase:
        return (f"{char} ia a lowercase letter")
    else:
        return (f"{char} is not  character")
    
x = input("Enter the character: ")
print(case(x))