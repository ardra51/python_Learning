# Student Marks Analyzer

marks = []   # list to store marks

print("Enter student marks (Enter -1 to stop):")

# Loop to take input
while True:
    mark = float(input("Enter mark: "))

    if mark == -1:
        break   # stop input

    if mark < 0 or mark > 100:
        print("Invalid mark! Enter between 0 and 100.")
        continue  # skip invalid input

    marks.append(mark)

# Check if list is empty
if len(marks) == 0:
    print("No data entered!")
else:
    total = 0

    # Loop to calculate total
    for m in marks:
        total += m

    average = total / len(marks)

    print("\n--- Results ---")
    print("Total Students:", len(marks))
    print("Average Marks:", average)
    print("Highest Marks:", max(marks))
    print("Lowest Marks:", min(marks))

    # Grade assignment
    print("\nGrades:")
    for m in marks:
        if m >= 90:
            grade = "A"
        elif m >= 75:
            grade = "B"
        elif m >= 50:
            grade = "C"
        else:
            grade = "Fail"

        print("Marks:", m, "Grade:", grade)

        '''''''
        # Number Checker

numbers = []   # list (data type)

# Loop to take 5 numbers
for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

total = 0

# Loop to process numbers
for num in numbers:
    total += num

    # Control statement
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

print("Total sum is:", total)