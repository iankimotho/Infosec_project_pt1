import math

def volume(radius):
    radius = int(radius)
    if radius >= 0:
        volume = 4/3 * math.pi * radius ** 3
        return volume
    else:
        return (f"Invalid input")

radius = int(input(f"Enter the radius of the circle: "))
print(f"The volume of the circle is {volume(radius)}")