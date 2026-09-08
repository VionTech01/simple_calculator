
print("========== Simple Calculator ==========")

#Katika Calculator hii tutafanya hesabu kuu nne tu ambazo ni kujumlisha, kutoa, kuzidisha na kugawanya

#Additional Function
def addition():
    try:
        a = float(input("Enter Value of a: "))
        b = float(input("Enter Value of b: "))

        print(f"Results: {a + b}")
        return a + b

    except ValueError:
        print("Please enter number only")


#Substraction Function
def substraction():
    try:
        a = float(input("Enter Value of a: "))
        b = float(input("Enter Value of b: "))

        print(f"Results: {a - b}")
        return a - b
        

    except ValueError:
        print("Please enter number only")


#Multiplication Function
def multiplication():
    try:
        a = float(input("Enter Value of a: "))
        b = float(input("Enter Value of b: "))
        
        print(f"Results: {a * b}")
        return a * b

    except ValueError:
        print("In This Version We Allow Only Numbers!")



#Division Function
def division():
    try:
        a = float(input("Enter Value of a: "))
        b = float(input("Enter Value of b: "))
        
        if b == 0:
            print("Can't Divide by Zero!")
        
        else:
            print(f"Results: {a / b}")
            return a / b

    except ValueError:
        print("Please enter number only")


#Calculator Menu
def calculator():
    print("========== Simple Calculator Menu ==========")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("Enter Your Choice: ")
        if choice == "1":
            addition()

        elif choice == "2":
            substraction()

        elif choice == "3":
            multiplication()

        elif choice == "4":
            division()

        elif choice == "5":
            print("Thanks for Choosing our Calculator")
            break

        else:
            print("Wrong Input")


calculator()




    