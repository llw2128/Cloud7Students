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
        for student in self.students:
            if student["uni"] == uni:
                return student
        return f"Student not found for uni {uni}"
    
    def delete_student(self, uni):
        for i in range(0, len(self.students)):
            student = self.students[i]
            if student["uni"] == uni:
                self.students.remove(student)
                with open(self.students_file, 'w') as f:
                    json.dump(self.students, f, indent=4)
                return f"Deleted student with uni {uni} {student}"
        return f"Student not found for uni {uni}"

    """
    Calling the same PUT request multiple times will always 
    produce the same result
    """
    def put_student(self, uni, student):
        print(student)
        studentToAdd = self.student_to_json(student)
        print(studentToAdd)
        found = False
        for i in range(0, len(self.students)):
            student = self.students[i]
            if student["uni"] == uni: # Found so replace
                self.students[i] = studentToAdd
                found = True
        if found is False:
            self.students.append(studentToAdd)
        with open(self.students_file, 'w') as f:
                json.dump(self.students, f, indent=4)
        return studentToAdd
    
    """
    Calling a POST request repeatedly have side effects of 
    creating the same resource multiple times
    """
    def post_student(self, uni, student):
        student = self.student_to_json(student)
        self.students.append(student)
        with open(self.students_file, 'w') as f:
                json.dump(self.students, f, indent=4)
        return student
