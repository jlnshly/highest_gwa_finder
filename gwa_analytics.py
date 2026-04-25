class GradeProcessor:
    """Will do all the math or processing for finding the highest gwa"""
    def __init__(self, student_list):
        self.students = student_list

    def find_highest_gwa(self):
        if not self.students:
            return None
        return min(self.students, key=lambda s: s.gwa)

