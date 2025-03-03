def calculate_grade(class_standing, major_exam):
    return round((class_standing * 0.6) + (major_exam * 0.4), 2)

def load_records():
    return []

def save_records():
    print("Records saved.")

def show_all(records):
    for record in records:
        print(record)

def order_by_lastname(records):
    return sorted(records, key=lambda x: x[1][1])

def order_by_grade(records):
    return sorted(records, key=lambda x: calculate_grade(x[2], x[3]), reverse=True)

def show_student(records, student_id):
    for record in records:
        if record[0] == student_id:
            print(record)
            return
    print("Student not found.")

def add_record(records):
    student_id = input("Enter Student ID (6-digit): ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input("Enter New First Name: ") or record[1][0]
            last_name = input("Enter New Last Name: ") or record[1][1]
            class_standing = input("Enter New Class Standing: ") or record[2]
            major_exam = input("Enter New Major Exam Grade: ") or record[3]
            records[i] = (student_id), (first_name, last_name), float(class_standing), float(major_exam)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record(records, student_id):
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return
    print("Student not found.")

def main():
    records = load_records()
    
    while True:
        print("\nMenu:")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            show_all(records)
        elif choice == '2':
            sorted_records = order_by_lastname(records)
            show_all(sorted_records)
        elif choice == '3':
            sorted_records = order_by_grade(records)
            show_all(sorted_records)
        elif choice == '4':
            student_id = input("Enter Student ID: ")
            show_student(records, student_id)
        elif choice == '5':
            add_record(records)
        elif choice == '6':
            student_id = input("Enter Student ID to edit: ")
            edit_record(records, student_id)
        elif choice == '7':
            student_id = input("Enter Student ID to delete: ")
            delete_record(records, student_id)
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
