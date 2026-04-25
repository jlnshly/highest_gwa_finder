import os
from student_information import Student
from gwa_analytics import GradeProcessor

def execute():
    if not os.path.exists('students.txt'):
        print('No students.txt found')
    with open('students.txt', 'r') as f:
        lines = f.readlines()
    student_objects = []
    for line in lines:
        try:
            first_name, last_name, gwa = line.strip().split(',')
            student_objects.append(Student(first_name.strip(), last_name.strip(), float(gwa.strip())))
        except ValueError:
            continue
    engine = GradeProcessor(student_objects)
    highest = engine.find_highest_gwa()
    if highest:
        for h in highest:
            print(f'{h.last_name}, {h.first_name} with {h.gwa}')

    else:
        print('Student information is not available')

if __name__ == '__main__':
    execute()

