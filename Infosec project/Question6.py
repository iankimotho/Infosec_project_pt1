values = []

for i in range(5):
    val = float(input(f"Enter the value {i+1}: "))
    values.append(val)

average = sum(values) / 5
print("Average: ", average)