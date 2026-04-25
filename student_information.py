class Student:
    """Keeping student records"""
    def __init__(self, first_name = str, last_name = str, gwa = float):
        self.first_name = first_name
        self.last_name = last_name
        self.gwa = gwa

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.gwa}'


