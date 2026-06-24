
    
      
while True:

    name = input("Enter the student name: ")

    m1 = int(input("Enter mark 1: "))
    m2 = int(input("Enter mark 2: "))
    m3 = int(input("Enter mark 3: "))

    total = m1 + m2 + m3
    average = total / 3

    print("Student name =", name)
    print("Total =", total)
    print("Average =", average)

    if average >= 90:
        print("Grade A")

    elif average >= 70:
        print("Grade B")

    elif average >= 50:
        print("Grade C")

    else:
        print("Fail")

    choice = input("Do you want to continue (yes/no): ")

    if choice.lower() == "no":
        print("Program ended")
        break
