numbers = []

def add_number(value):
    number = int(value)
    numbers.append(number)

def get_number():
    return numbers

def get_summary():
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    return count, total, average

def clear_numbers():
    numbers.clear()
    