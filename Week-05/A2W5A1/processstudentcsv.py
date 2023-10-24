import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
'''


def validate_data(line):
    # WRITE YOUR SOLUTION HERE:
    student_number, first_name, last_name, date_of_birth, study_program, = line.split(",")
    invalid_data = []
    courses = ["INF", "TINF", "CMD", "AI"]

    if len(student_number) != 7 or student_number[0] != "0" or student_number[1] != "8" and student_number[1] != "9":
        invalid_data.append(student_number)
    if not first_name.isalpha():
        invalid_data.append(first_name)
    if not last_name.isalpha():
        invalid_data.append(last_name)
    if len(date_of_birth) != 10 or date_of_birth[4] != '-' or date_of_birth[7] != '-':
        invalid_data.append(date_of_birth)
    elif int(date_of_birth[:4]) < 1960 or int(date_of_birth[:4]) > 2004:
        invalid_data.append(date_of_birth)
    elif int(date_of_birth[5:7]) < 1 or int(date_of_birth[5:7]) > 12:
        invalid_data.append(date_of_birth)
    elif int(date_of_birth[8:10]) < 1 or int(date_of_birth[8:10]) > 31:
        invalid_data.append(date_of_birth)
    if study_program not in courses: 
        invalid_data.append(study_program)

    if not invalid_data:
        valid_lines.append(line)
    elif invalid_data:
        corrupt_lines.append(line + " => INVALID DATA: " + str(invalid_data))


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')