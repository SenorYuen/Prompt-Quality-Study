class AssessmentSystem:
    def __init__(self):
        # Initialize the students dictionary in the assessment system
        self.students = {}

    def add_student(self, name, grade, major):
        # Add a new student into self.students dictionary
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        # Add score of specific course for student in self.students
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        # Get average grade of one student
        if name in self.students and self.students[name]['courses']:
            total_score = sum(self.students[name]['courses'].values())
            return total_score / len(self.students[name]['courses'])
        else:
            return None

    def get_all_students_with_fail_course(self):
        # Get all students who have any score below 60
        fail_students = []
        for student, info in self.students.items():
            for score in info['courses'].values():
                if score < 60:
                    fail_students.append(student)
                    break
        return fail_students

    def get_course_average(self, course):
        # Get the average score of a specific course
        total_score = 0
        count = 0
        for student, info in self.students.items():
            if course in info['courses']:
                total_score += info['courses'][course]
                count += 1
        if count > 0:
            return total_score / count
        else:
            return None

    def get_top_student(self):
        # Calculate every student's gpa and find the student with highest gpa
        top_student = None
        top_gpa = 0
        for student, info in self.students.items():
            gpa = self.get_gpa(student)
            if gpa is not None and gpa > top_gpa:
                top_gpa = gpa
                top_student = student
        return top_student