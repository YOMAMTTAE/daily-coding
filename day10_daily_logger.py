from datetime import date

def summarize(numbers):
    count = len(numbers)
    total = sum(numbers)
    average = total / count if count > 0 else 0
    return count, total, average

numbers = []

print("daily number logger")
print("enter numbers. type 'q' to finish. \n ")

while True:
    value = input("enter number (or q):")

    if value == "q":
        break

    number = int(value)
    numbers.append(number)

count, total, average = summarize(numbers)
today = date.today()

with open("daily_log.txt", "a", encoding="utf-8") as file:
    file.write(f"date: {today}\n")
    file.write(f"numbers: {numbers}\n")
    file.write(f"count: {count}\n")
    file.write(f"total: {total}\n")
    file.write(f"average: {average}\n")
    file.write("-"*20+"\n")

print("\nsummary") 
print("date:", today)
print("numbers:", numbers)
print("count:", count)
print("total:", total)
print("average:", average)
          
