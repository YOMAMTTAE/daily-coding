numbers = []

while True:
    value = input("enter a number (or q to quit): ")

    if value == "q":
        break

    number = int(value)
    numbers.append(number)

print("numbers:", numbers)
print("count:", len(numbers))
print("total:", sum(numbers))
