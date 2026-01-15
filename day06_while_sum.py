total = 0 

while True:
    value = input("enter a number(or q to quit)")
    if value == "q":
        break

    number = int(value)
    total = total + number

print("total sum:", total)

