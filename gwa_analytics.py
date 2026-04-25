class GradeProcessor:
    """Will do all the math or processing for finding the highest gwa"""
    def __init__(self, student_list):
        self.students = student_list

    def find_highest_gwa(self):
        if not self.students:
            return []
        best_gwa = min(students.gwa for students in self.students)
        highest = [s for s in self.students if s.gwa == best_gwa]
        return highest

