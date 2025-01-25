# Drawing patterns exercise
from colorama import Fore
from colorama import Style

# Colorama was imported to bring some colour to the shapes
while True:
    print("🌟 Welcome to the Python Pattern Drawing Program!")
    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Heart with Hollow Center")
    print("10. Number Pyramid")

    try:
        choice = int(input("Enter the number corresponding to your choice: "))
    except ValueError:
        print()
        print(Fore.RED + "Please enter a valid number.")
        print(Style.RESET_ALL)
        continue
    # An error handling method was implemented.

    if choice == 1:  # Right-angled Triangle

        num = int(input("Enter the number of rows: "))

        for a in range(1, num + 1):
            for b in range(1, a + 1):
                print(Fore.CYAN + '*', end=' ')
            print(Style.RESET_ALL)

    elif 2 == choice:  # Square with Hollow Center

        num = int(input("Enter the number of rows: "))

        for rows in range(1, num + 1):
            for columns in range(1, num + 1):
                if rows == 1 or rows == num or columns == 1 or columns == num:
                    print(Fore.CYAN + "*", end=" ")
                else:
                    print(Fore.CYAN + " ", end=" ")
            print(Style.RESET_ALL)

    elif choice == 3:  # Diamond

        rows = int(input("Enter the number of rows: "))

        for num in range(rows + 1):
            print(Fore.CYAN + " " * (rows - num) + "* " * num)
        for num in range(1, rows + 1):
            print(Fore.CYAN + " " * num + "* " * (rows - num))
        print(Style.RESET_ALL)

    elif choice == 4:  # Left-angled Triangle

        num = int(input("Enter the number of rows: "))
        for a in range(num + 1, 0, -1):
            for b in range(1, a + 1):
                print(Fore.CYAN + '*', end=' ')
            print(Style.RESET_ALL)

    elif choice == 5:  # Hollow Square

        num = int(input("Enter the number of rows: "))
        for rows in range(1, num + 1):
            for columns in range(1, num + 1):
                if rows == 1 or rows == num or columns == 1 or columns == num:
                    print(Fore.CYAN + "*", end=" ")
                else:
                    print(Fore.CYAN + " ", end=" ")
            print(Style.RESET_ALL)

    elif choice == 6:  # Pyramid

        rows = int(input("Enter the number of rows: "))

        for num in range(rows + 1):
            print(Fore.CYAN + " " * (rows - num) + "* " * num)
        print(Style.RESET_ALL)

    elif choice == 7:  # Reverse Pyramid

        rows = int(input("Enter the number of rows: "))

        for num in range(1, rows + 1):
            print(" " * num + "* " * (rows - num))

    elif choice == 8:  # Rectangle with Hollow Center

        height = int(input("Enter the height of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))

        for h in range(1, height + 1):
            for w in range(1, width + 1):
                if h == 1 or w == 1 or h == height or w == width:
                    print(Fore.CYAN + "*", end=" ")
                else:
                    print(Fore.CYAN + " ", end=" ")
            print(Style.RESET_ALL)

    elif choice == 9:  # Heart Shape // no rows choice possible :(

        for row in range(6):
            for col in range(7):
                if row == 0 and col % 3 != 0:
                    print(Fore.LIGHTRED_EX + "*", end=" ")
                elif row == 1 and col % 3 == 0:
                    print(Fore.LIGHTRED_EX + "*", end=" ")
                elif row == 2 and (col == 6 or col == 0):
                    print(Fore.LIGHTRED_EX + "*", end=" ")
                elif row == 3 and (col == 5 or col == 1):
                    print(Fore.LIGHTRED_EX + "*", end=" ")
                elif row == 4 and (col == 4 or col == 2):
                    print(Fore.LIGHTRED_EX + "*", end=" ")
                elif row == 5 and col == 3:
                    print(Fore.LIGHTRED_EX + "*", end=" ")
                else:
                    print(Fore.LIGHTRED_EX + " ", end=" ")
            print(Style.RESET_ALL)

    elif choice == 10:  # Number Pyramid

        number = int(input("Enter number of rows: "))

        for a in range(1, number + 1):
            for b in range(1, number - a + 1):
                print(" ", end=" ")
            for b in range(a, 0, -1):
                print(b, end=" ")
            for b in range(2, a + 1):
                print(b, end=" ")

            print()
    else:
        print("We're sorry, but we do not have such option.")

    restart = input("Do you want to draw another pattern? (yes/no): ").strip().lower()

    while restart != 'yes' and restart != 'no':
        print()
        print(Fore.LIGHTRED_EX + "Please enter 'yes' or 'no'.")
        print(Style.RESET_ALL)
        restart = input("Do you want to draw another pattern? (yes/no): ").strip().lower()

    if restart == 'yes':
        print("Okay, let's take you back up!")
        continue

    elif restart == 'no':
        print()
        print(Fore.LIGHTMAGENTA_EX + "Goodbye! <3")
        print(Style.RESET_ALL)
        break