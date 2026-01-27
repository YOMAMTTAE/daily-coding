def summarize_numbers(numbers):
    count=len(numbers)
    total=sum(numbers)
    return count, total

numbers=[]

while True:
    value = input("enter a number(or q to quit)")

    if value == "q":
        break

    number = int(value)
    numbers.append(number)

count, total = summarize_numbers(numbers)

print("numbers:", numbers)
print("count:", count)
print("total:", total)

