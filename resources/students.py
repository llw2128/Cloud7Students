import json


class StudentsResource:
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    students_file = \
        "./resources/mockStudents.json"

    def __init__(self):
        self.students = None

        with open(self.students_file, "r") as j_file:
            self.students = json.load(j_file)

    def get_students(self):
        return self.students

    def get_specific_student(self, uni):
        try:
            return self.students[uni]
        except KeyError:
            return f"Student not found for uni {uni}"
    
    def delete_student(self, uni):
        try:
            deleted_student = self.students.pop(uni)
            with open(self.students_file, 'w') as f:
                json.dump(self.students, f)
            return deleted_student
        except KeyError:
            return f"Student not found for uni {uni}"