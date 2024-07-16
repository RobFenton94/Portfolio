# Lists created to outline client names and dates of birth.
names = []
birthdays = []

# Open the client's data in read mode.
with open('DOB.txt', 'r') as file:
    # Read lines and store them in a list.
    lines = file.readlines()

# Now we process each line in the list.
for line in lines:
    # Splitting each line into their respective categories.
    line = line.strip()
    # Strip to remove any potential whitespace around client's data.
    if line:  # Checking that the line is not empty.
        data = line.split(' ')  # Splitting by space.
        name = ' '.join(data[:-3])  # Joining the name parts.
        birthday = ' '.join(data[-3:])  # Joining the birthday parts.
        # Adding names and birthdates to their respective lists.
        names.append(name.strip())  # Remove whitespace.
        birthdays.append(birthday.strip())  # Remove whitespace.

# Printing the results.
print("Names:")
for name in names:
    print(name)

print("\nDates of Birth:")
for birthday in birthdays:
    print(birthday)
