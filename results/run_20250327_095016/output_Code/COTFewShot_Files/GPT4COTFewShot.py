class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        self.students[name] = {
            'name': name,
            'grade': grade,
            'major': major,
            'courses': {}
        }

    def add_course_score(self, name, course, score):
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        if name in self.students:
            courses = self.students[name]['courses']
            if courses:
                return sum(courses.values()) / len(courses)
        return None

    def get_all_students_with_fail_course(self):
        failed_students = []
        for student in self.students.values():
            if any(score < 60 for score in student['courses'].values()):
                failed_students.append(student['name'])
        return failed_students

    def get_course_average(self, course):
        total_score = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                total_score += student['courses'][course]
                count += 1
        return total_score / count if count > 0 else None

    def get_top_student(self):
        top_student = None
        highest_gpa = 0
        for student in self.students.values():
            gpa = self.get_gpa(student['name'])
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = student['name']
        return top_student