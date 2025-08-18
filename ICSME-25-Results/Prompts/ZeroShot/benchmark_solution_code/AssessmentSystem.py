'''
# This is a class as an student assessment system, which supports add student, add course score, calculate GPA, and other functions for students and courses.

class AssessmentSystem:
    def __init__(self):
        """
        Initialize the students dict in assessment system.
        """

    def add_student(self, name, grade, major):
        """
        Add a new student into self.students dict
        """

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        """

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score blow 60
        :return: list of str ,student name
        """

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """


'''


class AssessmentSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade, major):
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        if name in self.students and self.students[name]['courses']:
            return sum(self.students[name]['courses'].values()) / len(self.students[name]['courses'])
        else:
            return None

    def get_all_students_with_fail_course(self):
        students = []
        for name, student in self.students.items():
            for course, score in student['courses'].items():
                if score < 60:
                    students.append(name)
                    break
        return students

    def get_course_average(self, course):
        total = 0
        count = 0
        for student in self.students.values():
            if course in student['courses']:
                score = student['courses'][course]
                if score is not None:
                    total += score
                    count += 1
        return total / count if count > 0 else None

    def get_top_student(self):
        top_student = None
        top_gpa = 0
        for name, student in self.students.items():
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > top_gpa:
                top_gpa = gpa
                top_student = name
        return top_student

