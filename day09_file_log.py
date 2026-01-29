def summarize_numbers(numbers):
    count = len(numbers)
    total = sum(numbers)
    return count, total

numbers = []

while True:
    value = input("enter a number (or q to quit)")

    if value == "q":
        break

    number = int(value)
    numbers.append(number)

count, total = summarize_numbers(numbers)

with open("result.txt","w",encoding="utf-8")as file:
    file.write(f"numbers:{numbers}\n")
    file.write(f"count:{count}\n")
    file.write(f"total:{total}\n")

print("nsaved result:")
with open("result.txt","r",encoding="utf-8") as file:
    content = file.read()
    print(content)

