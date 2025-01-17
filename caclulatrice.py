import os

# Function to add numbers
def addition():
    nbr1 = input("Enter the first number: ")
    nbr2 = input("Enter the second number: ")
    result = float(nbr1) + float(nbr2)
    operation = f"{nbr1} + {nbr2} = {result}"
    print(operation)
    history(operation)

# Function to subtract numbers
def subtraction():
    nbr1 = input("Enter the first number: ")
    nbr2 = input("Enter the second number: ")
    result = float(nbr1) - float(nbr2)
    operation = f"{nbr1} - {nbr2} = {result}"
    print(operation)
    history(operation)

# Function to multiply numbers
def multiplication():
    nbr1 = input("Enter the first number: ")
    nbr2 = input("Enter the second number: ")
    result = float(nbr1) * float(nbr2)
    operation = f"{nbr1} x {nbr2} = {result}"
    print(operation)
    history(operation)

# Function to divide numbers
def division():
    nbr1 = input("Enter the first number: ")
    nbr2 = input("Enter the second number: ")
    try:
        result = float(nbr1) / float(nbr2)
        operation = f"{nbr1} / {nbr2} = {result}"
        print(operation)
        history(operation)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Function to save history
def history(operation, file="history.txt"):
    with open(file, "a") as f:
        f.write(operation + "\n")

# Function to display history
def display_history(file="history.txt"):
    if not os.path.exists(file):
        print("\nNo history available.")
        return

    print("\n=== CALCULATION HISTORY ===")
    with open(file, "r") as f:
        for line in f:
            print(line.strip())

# Menu function
def menu():
    while True:
        print("\nMenu:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: History")
        print("6: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            display_history()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, 5, or 6.")

# Start the program
menu()
