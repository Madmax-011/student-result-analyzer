student = {}

while True:
    print("\n-- Student Manager App --")
    print("1. Add Student")
    print("2. View Students")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add student
    if choice == "1":
        name = input("Enter the name: ")
        marks = int(input("Enter the marks: "))
        student[name] = marks
        print(f"{name} successfully added.")

    # View students
    elif choice == "2":
        if not student:
            print("No students found.")
        else:
            for name, marks in student.items():
                print(name, ":", marks)

    # Check result
    elif choice == "3":
        name = input("Enter the name: ")

        if name in student:
            marks = student[name]

            if marks >= 40:
                print(f"{name},marks = {marks} is Pass")
            else:
                print(f"{name},marks = {marks} is Fail")
        else:
            print("Student not found.")

    # Exit
    elif choice == "4":
        print("Successfully Exited.")
        break

    else:
        print("Invalid choice.")


        dsfgswadhfgswad