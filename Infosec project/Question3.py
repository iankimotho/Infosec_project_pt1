def area(length):
    length = int(length)
    if length >= 0:
        area = length ** 2
        return area
    else:
        return(f"Invalid input")
    
def perimeter(length):
    length = int(length)
    if length >= 0:
        per = length * 4
        return per
    else:
        return(f"Invalid input")

length = int(input("Enter the length of the square: "))
print(f"Perimeter: {perimeter(length)}")
print(f"Area: {area(length)}")