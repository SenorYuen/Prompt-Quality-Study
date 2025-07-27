class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        if name not in self.students:
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
        if name in self.students and self.students[name]['courses']:
            total_score = sum(self.students[name]['courses'].values())
            num_courses = len(self.students[name]['courses'])
            return total_score / num_courses
        return None

    def get_all_students_with_fail_course(self):
        students_with_fail = []
        for student in self.students.values():
            if any(score < 60 for score in student['courses'].values()):
                students_with_fail.append(student['name'])
        return students_with_fail

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
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name
        return top_student