students = []

def add_student():
    name = input("Enter student name: ")
    score = int(input("Enter score: "))
    
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "F"
    
    student = {
        "name": name,
        "score": score,
        "grade": grade
    }
    
    students.append(student)
    print("Student added successfully!")


def display_students():
    print("\n--- Student Records ---")
    
    for student in students:
        print("Name:", student["name"])
        print("Score:", student["score"])
        print("Grade:", student["grade"])
        print("-------------------")


def main():
    while True:
        print("\n1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")


main()