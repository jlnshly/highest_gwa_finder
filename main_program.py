import os
from student_information import Student
from gwa_analytics import GradeProcessor

def execute():
    with open('students.txt', 'r') as f:
        lines = f.readlines()
    student_objects = []
    for line in lines:
        first_name, last_name, gwa = line.strip().split(',')
        student_objects.append(Student(first_name.strip(), last_name.strip(), float(gwa.strip())))
    engine = GradeProcessor(student_objects)
    winner = engine.find_highest_gwa()
    print(f'{winner.first_name} {winner.last_name} with {winner.gwa}')


