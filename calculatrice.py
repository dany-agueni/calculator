#Funtion to do an addition
def addition():
    nbr1=input("Enter the first number: ")
    nbr2=input("Enter the second number: ")
    result= float(nbr1) + float(nbr2)
    print(f" {nbr1} + {nbr2} = {result}")
#Funtion to do a subtraction
def subtraction():
    nbr1=input("Enter the first number: ")
    nbr2=input("Enter the second number: ")
    result= float(nbr1) - float(nbr2)
    print(f" {nbr1} - {nbr2} = {result}")
#Funtion to do a multiplication
def multiplication():
    nbr1=input("Enter the first number: ")
    nbr2=input("Enter the second number: ")
    result= float(nbr1) * float(nbr2)
    print(f" {nbr1} x {nbr2} = {result}")
#Funtion to do a division
def division():
    nbr1=input("Enter the first number: ")
    nbr2=input("Enter the second number: ")
    result= float(nbr1) / float(nbr2)
    print(f" {nbr1} / {nbr2} = {result}")
#Funtion to do the menu
def menu():
    while True:
        print("\nMenu:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication() 
        elif choice =="4":
            division()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4 or 5")
#Calling the menu to start the program
menu()
