marks = []
average = 0.0
print("-----------------------------------------")
print("       STUDENT PROGRESS TRACKER SYSTEM   ")
print("-----------------------------------------")
name = input("enter Your Student Name : ")
student_class = input("enter your Class : ")
roll = input("enter your Roll Number : ")
total = 0
num_sub = int(input("how many subjects do you want to enter : "))
for i in range(num_sub):
    m = int(input(f"enter marks for subject {i+1}: "))
    marks.append(m)
    total += m
average = total / num_sub


def avg(average):
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    elif average >= 35:
        grade = "D"
    else:
        grade = "Fail"
    return grade

grade = avg(average)

def pass_fail(marks):
    result = "PASS"
    for m in marks:
        if m < 35:
            result = "FAIL"
            break
    return result

result = pass_fail(marks)

def report(name, student_class, roll, total, average, grade, result):
    print("\n-----------------------------------------")
    print("        STUDENT PROGRESS REPORT           ")
    print("-----------------------------------------")
    print(f"Name        : {name}")
    print(f"Class       : {student_class}")
    print(f"Roll No     : {roll}")
    print(f"Total Marks : {total}")
    print(f"Average     : {average:.2f}")
    print(f"Grade       : {grade}")
    print(f"Result      : {result}")
    print("-----------------------------------------\n")


while True:
    avg(average)
    pass_fail(marks)
    report(name, student_class, roll, total, average, grade, result)
    print("What do you want to do next?")
    print("1. Enter marks again")
    print("2. View report again")
    print("3. Exit")

    choice = input("enter your choice: ")

    if choice == "1":
        total = 0
        marks = []
        num_sub = int(input("how many subjects do you want to enter : "))
        for i in range(num_sub):
            m = int(input(f"enter marks for subject {i+1}: "))
            marks.append(m)
            total += m
        average = total / num_sub
        grade = avg(average)
        result = pass_fail(marks)
        

    elif choice == "2":
        report(name, student_class, roll, total, average, grade, result)

    elif choice == "3":
        print("\nExiting the system... Thank you!")
        break

    else:

        print("Invalid choice! Returning to menu...\n")

print("thank you have a good day!")
