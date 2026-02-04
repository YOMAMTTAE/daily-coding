numbers = []

def show_menu():
    print("\n=== number manager ===")
    print("1. add number")
    print("2. show numbers")
    print("3. show summary")
    print("4. exit")

while True:
    show_menu()
    choice = input("select menu(1-4):")

    if choice == "1":
        value = input("enter nubers:")
        try:
            number = int(value)
            numbers.append(number)
            print("number added.")
        except valueerror:
            print("invalid number.")

    elif choice == "2":
        print("numbers:", numbers)


    elif choice == "3":
        if len(numbers) == 0:
            print("no numbers yet.")
        else:
            total = sum(numbers)
            average = total / len(numbers)
            print("count:", len(numbers))
            print("total:", total)
            print("average:", average)
    
    elif choice == "4":
        print("program exited.")
        break

    else:
        print("invalid menu selection.")
        
