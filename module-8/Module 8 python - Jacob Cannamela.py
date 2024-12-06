# Jacob Cannamela
# CSD325
# 12/6/2024
# Module 8 python assignment


import json

# Load JSON file into a Python class list
with open("student.json", "r") as file:
    students = json.load(file)

# Function to print the current student list
def print_students(students_list):
    print("Updated Student List:")
    for student in students_list:
        print(f"{student['F_Name']} {student['L_Name']} : ID = {student['Student_ID']}, Email = {student['Email']}")

# Display the original list
print("This is the original Student list.")
print_students(students)

# Add a new student to the list
new_student = {
    "F_Name": "Jacob", 
    "L_Name": "Cannamela",  
    "Student_ID": 911911,      
    "Email": "thatsagoodemail@emailme.com"  
}

# Using .append function to write the newly defined student to the list
students.append(new_student)

# Display the list has been updated
print("Notification: The Student list has been updated.")

# Show updated list
print_students(students)

# Save the updated list
with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

# Display the JSON file has been updated
print("Notification: The student.json file has been updated.")
