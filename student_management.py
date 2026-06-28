import csv
import json
import logging
import os
from datetime import datetime

# Custom Exception
class StudentNotFoundError(Exception):
    """Custom exception for when a student is not found."""
    pass

# Setup logging
logging.basicConfig(
    filename='student_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

CSV_FILE = 'students.csv'
JSON_FILE = 'students.json'

def initialize_files():
    """Initialize CSV and JSON files if they don't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['reg_number', 'name', 'age', 'grade'])
        logging.info("Initialized students.csv")
    
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'w') as f:
            json.dump({}, f, indent=4)
        logging.info("Initialized students.json")

def load_students_csv():
    """Load students from CSV file."""
    students = []
    try:
        with open(CSV_FILE, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        logging.error("CSV file not found during load.")
    except Exception as e:
        logging.error(f"Error loading CSV: {str(e)}")
    return students

def save_student_csv(student):
    """Append a new student to CSV."""
    try:
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([student['reg_number'], student['name'], student['age'], student['grade']])
        logging.info(f"Added student to CSV: {student['reg_number']}")
    except Exception as e:
        logging.error(f"Error saving to CSV: {str(e)}")
        raise

def load_additional_details():
    """Load additional details from JSON."""
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except Exception as e:
        logging.error(f"Error loading JSON: {str(e)}")
        return {}

def save_additional_details(details):
    """Save additional details to JSON."""
    try:
        with open(JSON_FILE, 'w') as f:
            json.dump(details, f, indent=4)
        logging.info("Saved additional details to JSON")
    except Exception as e:
        logging.error(f"Error saving JSON: {str(e)}")
        raise

def add_student():
    """Add a new student."""
    try:
        reg_number = input("Enter registration number: ").strip()
        if not reg_number:
            raise ValueError("Registration number cannot be empty.")
        
        name = input("Enter name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        
        age = int(input("Enter age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        grade = input("Enter grade: ").strip()
        if not grade:
            raise ValueError("Grade cannot be empty.")
        
        address = input("Enter address: ").strip()
        contact = input("Enter contact: ").strip()
        program = input("Enter program: ").strip()
        
        student = {
            'reg_number': reg_number,
            'name': name,
            'age': str(age),
            'grade': grade
        }
        
        # Check if reg_number already exists
        students = load_students_csv()
        if any(s['reg_number'] == reg_number for s in students):
            raise ValueError(f"Student with reg_number {reg_number} already exists.")
        
        save_student_csv(student)
        
        details = load_additional_details()
        details[reg_number] = {
            'address': address,
            'contact': contact,
            'program': program
        }
        save_additional_details(details)
        
        print("Student added successfully!")
        logging.info(f"Student added: {reg_number}")
    except ValueError as ve:
        print(f"Input error: {ve}")
        logging.warning(f"Input error in add_student: {ve}")
    except Exception as e:
        print("An error occurred while adding student.")
        logging.error(f"Error in add_student: {str(e)}")
    finally:
        print("Add operation completed.")

def view_students():
    """View all students."""
    try:
        students = load_students_csv()
        details = load_additional_details()
        
        if not students:
            print("No students found.")
            return
        
        print("\nStudent Records:")
        print("-" * 80)
        for student in students:
            reg = student['reg_number']
            add_detail = details.get(reg, {})
            print(f"Reg: {reg}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
            print(f"Address: {add_detail.get('address', 'N/A')}, Contact: {add_detail.get('contact', 'N/A')}, Program: {add_detail.get('program', 'N/A')}")
            print("-" * 40)
    except Exception as e:
        print("Error viewing students.")
        logging.error(f"Error in view_students: {str(e)}")
    finally:
        print("View operation completed.")

def search_student():
    """Search for a student by reg number."""
    try:
        reg_number = input("Enter registration number to search: ").strip()
        if not reg_number:
            raise ValueError("Registration number cannot be empty.")
        
        students = load_students_csv()
        details = load_additional_details()
        
        student = next((s for s in students if s['reg_number'] == reg_number), None)
        
        if not student:
            raise StudentNotFoundError(f"Student with reg_number {reg_number} not found.")
        
        add_detail = details.get(reg_number, {})
        print("\nStudent Found:")
        print(f"Reg: {student['reg_number']}, Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")
        print(f"Address: {add_detail.get('address', 'N/A')}, Contact: {add_detail.get('contact', 'N/A')}, Program: {add_detail.get('program', 'N/A')}")
    except StudentNotFoundError as snfe:
        print(snfe)
        logging.info(str(snfe))
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Error searching student.")
        logging.error(f"Error in search_student: {str(e)}")
    finally:
        print("Search operation completed.")

def update_student():
    """Update student details."""
    try:
        reg_number = input("Enter registration number to update: ").strip()
        if not reg_number:
            raise ValueError("Registration number cannot be empty.")
        
        students = load_students_csv()
        student_index = next((i for i, s in enumerate(students) if s['reg_number'] == reg_number), None)
        
        if student_index is None:
            raise StudentNotFoundError(f"Student with reg_number {reg_number} not found.")
        
        print("Enter new details (leave blank to keep current):")
        name = input(f"Name ({students[student_index]['name']}): ").strip()
        age_str = input(f"Age ({students[student_index]['age']}): ").strip()
        grade = input(f"Grade ({students[student_index]['grade']}): ").strip()
        
        if name:
            students[student_index]['name'] = name
        if age_str:
            age = int(age_str)
            if age < 0:
                raise ValueError("Age cannot be negative.")
            students[student_index]['age'] = str(age)
        if grade:
            students[student_index]['grade'] = grade
        
        # Update CSV
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['reg_number', 'name', 'age', 'grade'])
            writer.writeheader()
            writer.writerows(students)
        
        # Update JSON details
        details = load_additional_details()
        if reg_number in details:
            address = input(f"Address ({details[reg_number]['address']}): ").strip()
            contact = input(f"Contact ({details[reg_number]['contact']}): ").strip()
            program = input(f"Program ({details[reg_number]['program']}): ").strip()
            
            if address:
                details[reg_number]['address'] = address
            if contact:
                details[reg_number]['contact'] = contact
            if program:
                details[reg_number]['program'] = program
            save_additional_details(details)
        
        print("Student updated successfully!")
        logging.info(f"Student updated: {reg_number}")
    except StudentNotFoundError as snfe:
        print(snfe)
        logging.info(str(snfe))
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print("Error updating student.")
        logging.error(f"Error in update_student: {str(e)}")
    finally:
        print("Update operation completed.")

def delete_student():
    """Delete a student."""
    try:
        reg_number = input("Enter registration number to delete: ").strip()
        if not reg_number:
            raise ValueError("Registration number cannot be empty.")
        
        students = load_students_csv()
        new_students = [s for s in students if s['reg_number'] != reg_number]
        
        if len(new_students) == len(students):
            raise StudentNotFoundError(f"Student with reg_number {reg_number} not found.")
        
        # Update CSV
        with open(CSV_FILE, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['reg_number', 'name', 'age', 'grade'])
            writer.writeheader()
            writer.writerows(new_students)
        
        # Update JSON
        details = load_additional_details()
        if reg_number in details:
            del details[reg_number]
            save_additional_details(details)
        
        print("Student deleted successfully!")
        logging.info(f"Student deleted: {reg_number}")
    except StudentNotFoundError as snfe:
        print(snfe)
        logging.info(str(snfe))
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("Error deleting student.")
        logging.error(f"Error in delete_student: {str(e)}")
    finally:
        print("Delete operation completed.")

def main_menu():
    """Display main menu and handle user choices."""
    initialize_files()
    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            logging.info("System exited.")
            break
        else:
            print("Invalid choice. Please try again.")
            logging.warning(f"Invalid menu choice: {choice}")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")
        logging.warning("Program interrupted by user.")
    except Exception as e:
        print("An unexpected error occurred.")
        logging.error(f"Unexpected error in main: {str(e)}")
    finally:
        print("Thank you for using the Student Management System.")
