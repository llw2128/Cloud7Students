import json


class StudentsResource:
    students_file = \
        "./resources/mockStudents.json"

    def __init__(self):
        self.students = None

        with open(self.students_file, "r") as j_file:
            self.students = json.load(j_file)

    def student_to_json(self, student):
        student_json = {'uni': student.uni,
                        'first_name': student.first_name,
                        'last_name': student.last_name,
                        'email': student.email,
                        'school': student.school,
                        'year': student.year
                        }      
        return student_json

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
            print(deleted_student)
            with open(self.students_file, 'w') as f:
                json.dump(self.students, f)
            return f"Deleted student with uni {uni} {deleted_student}"
        except KeyError:
            return f"Student not found for uni {uni}"

    """
    Calling the same PUT request multiple times will always 
    produce the same result
    """
    def put_student(self, uni, student):
        student = self.student_to_json(student)
        self.students[uni] = student
        with open(self.students_file, 'w') as f:
                json.dump(self.students, f)
        return student
        # return f"Put student with uni {uni} {student}"
    
    """
    Calling a POST request repeatedly have side effects of 
    creating the same resource multiple times
    """
    def post_student(self, uni, student):
        student = self.student_to_json(student)
        self.students[uni] = student
        with open(self.students_file, 'w') as f:
                json.dump(self.students, f)
        return student
        # return f"Post student with uni {uni} {student}"
