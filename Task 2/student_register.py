# Asking the user to input the number of students.
num_students = int(input("How many students are registering? "))

# Opening the file in write mode.
with open('reg_form.txt', 'w') as file:
    # Iterate through the students.
    for i in range(num_students):
        # User enters student number.
        student_id = input(f"Enter Student ID Number {i+1}: ")
        # Write the student ID followed by a dotted line.
        file.write(f"{student_id}\n")
        # Giving students enough whitespace to sign next to their student ID.
        file.write("--------" * len(student_id) + "\n")

# Print the result.
print("Registration complete, please review reg_form.txt for your register.")
