class AssessmentSystem:
    def __init__(self):
        """
        Initialize the students dict in assessment system.
        The dictionary will hold student names as keys, and each value will be another dictionary 
        containing 'grade', 'major', and 'courses' (which is a dictionary of course scores).
        """
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student into self.students dict.
        :param name: str, the student's name
        :param grade: str, the student's grade level
        :param major: str, the student's major
        """
        if name not in self.students:
            self.students[name] = {'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, the student's name
        :param course: str, the course name
        :param score: float, the score achieved in the course
        """
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, the student's name
        :return: float, the average grade if the student exists and has course grades, or None otherwise
        """
        if name in self.students:
            courses = self.students[name]['courses']
            if courses:
                return sum(courses.values()) / len(courses)
        return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60.
        :return: list of str, student names
        """
        failing_students = []
        for name, data in self.students.items():
            if any(score < 60 for score in data['courses'].values()):
                failing_students.append(name)
        return failing_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, the course name
        :return: float, average scores of this course if anyone has a score for this course, or None if no records exist.
        """
        total_score = 0
        count = 0
        for data in self.students.values():
            if course in data['courses']:
                total_score += data['courses'][course]
                count += 1
        return total_score / count if count > 0 else None

    def get_top_student(self):
        """
        Calculate every student's GPA with get_gpa method, and find the student with the highest GPA.
        :return: str, name of the student whose GPA is highest
        """
        top_student = None
        highest_gpa = 0
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name
        return top_student