class Student:
    """Keeping student records"""
    def __init__(self, first_name = str, last_name = str, gwa = float):
        self.first_name = first_name
        self.last_name = last_name
        self.gwa = gwa

    @classmethod
    def from_string(txt, raw_lines):
        """Create a Student object from a string"""
        try:
            first_name, last_name, gwa = raw_lines.split(',')
            return txt(last_name.strip(), first_name.strip(), gwa.strip())
        except (ValueError, IndexError):
            return None

