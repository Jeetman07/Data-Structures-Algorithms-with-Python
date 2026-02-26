# Student Grade Lookup Program

# Starting dictionary with example data
grades = {
    "Anna": 5,
    "Mikko": 4,
    "Sara": 3
}

while True:
    print("\n--- Student Grade System ---")
    print("1 - Add / Update a grade")
    print("2 - Search for a student's grade")
    print("3 - Print all students and grades")
    print("0 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = int(input("Enter grade: "))
        grades[name] = grade
        print(f"Grade saved for {name}.")

    elif choice == "2":
        name = input("Enter student name to search: ")
        if name in grades:
            print(f"{name}'s grade is {grades[name]}.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nAll students and grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Try again.")