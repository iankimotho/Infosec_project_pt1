def days_to_seconds(days):
    days = int(days)
    if days >= 0:
        seconds = days * 24 * 60 * 60
        return seconds
    else:
        return (f"Invalid input")

days = int(input(f"Enter the number of days: "))
print(f"The number of seconds in {days} days is {days_to_seconds(days)}") 