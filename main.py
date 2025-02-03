##########################
# CASH MACHINE SIMULATOR #
##########################

import os

os.system("clear")


def is_float(amount):
    try:
        float(amount)
        return True  # Successfully converted to float
    except ValueError:
        return False  # Not a valid float


def display_balance(balance):
    os.system("clear")
    print("*" * 20)
    print(f"Your balance is: £{balance:.2f}")
    print("*" * 20)


def deposit():
    os.system("clear")
    print("*" * 20)
    amount = input("Enter amount to deposited: £")

    if is_float(amount):
        amount = float(amount)
    else:
        os.system("clear")
        print("*" * 20)
        amount = input("Enter amount to deposited: £")

    amount = float(amount)

    if amount <= 0:

        os.system("clear")
        print("*" * 20)
        print("Not a valid amount!")
        print("*" * 20)
        return 0
    else:
        return amount


def withdrawal(balance):

    print("*" * 20)
    print(f"Your balance is: £{balance:.2f}")
    print("*" * 20)
    amount = input("Enter amount to withdraw: £")

    if is_float(amount):
        amount = float(amount)  # Safe to convert now
    else:
        os.system("clear")
        print("*" * 20)
        amount = input("Enter amount to withdraw: £")

    amount = float(amount)

    if amount >= balance or amount <= 0:
        os.system("clear")
        print("*" * 20)
        print("Not a valid amount!")
        print("*" * 20)

        return 0
    else:
        amount = amount

    print("*" * 20)
    os.system("clear")
    if not amount > 0:
        print("*" * 20)
        print("Please enter a positive number!")
        print("*" * 20)
        return 0
    elif amount > balance:
        print("*" * 20)
        print("You cannot withdraw more than your balance.")
        print("*" * 20)
        return 0
    else:
        return amount


print("*" * 20)
print("Welcome to your Banking App.")
print("*" * 20)


def main():
    balance = 0
    is_running = True
    while is_running:

        print("1. Display Balance")
        print("2.         Deposit")
        print("3.        Withdraw")
        print("4.            Exit")

        print("*" * 20)
        option = input("Enter an option: ")

        os.system("clear")
        if option not in "1234":
            print("*" * 20)
            print("Not a valid entry")
            print("*" * 20)
            continue
        elif option == "1":
            display_balance(balance)
        elif option == "2":
            balance += deposit()
        elif option == "3":
            balance -= withdrawal(balance)
        elif option == "4":
            is_running = False

    os.system("clear")
    print()
    print("*" * 20)
    print("Have a nice day!")
    print("*" * 20)
    print("\n\n")


if __name__ == "__main__":
    main()
