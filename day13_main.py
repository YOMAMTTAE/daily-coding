from menu import show_menu
import number_manager

while True:
    show_menu()
    choice = input("select menu (1-5):")

    if choice == "1":
        value = input("enter number:")
        try:
            number_manager.add_number(value)
            print("number added.")
        except ValueError:
            print("invaild number")

    elif choice == "2":
        print("numbers:", number_manager.get_number())

    elif choice == "3":
        count, total, avg=number_manager.get_summary()
        print("count", count)
        print("total:", total)
        print("average:", avg)

    elif choice == "4":
        number_manager.clear_numbers()
        print("all numbers cleared.")

    elif choice == "5":
        print("program exited.")
        break

    else:
        print("invalid menu selection")

