numbers = []

print("safe number logger")
print("enter numbers only. type 'q' to quit.\n" )

while True:
    value = input("enter number (or q):")

    if value == "q":
        break

    try:
        number = int(value)
        numbers.append(number)
    except ValueError:
        print("invalid input. please enter a number.")
        continue

print("\nresult")
print("numbers:", numbers)
print("count:", len(numbers))
print("total:", sum(numbers))

