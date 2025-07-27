class AssessmentSystem:
    """
    This is a class as a student assessment system, which supports adding students, adding course scores, calculating GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in the assessment system.
        """
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student into self.students dict.
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        """
        # Add a new student with an empty courses dictionary
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of a specific course for a student in self.students.
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        # Check if the student exists and add the course score
        if name in self.students:
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get the average grade of one student.
        :param name: str, student name
        :return: float, average grade or None if no courses
        """
        # Check if the student exists
        if name in self.students:
            courses = self.students[name]['courses']
            # Calculate GPA if the student has courses
            if courses:
                return sum(courses.values()) / len(courses)
        return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60.
        :return: list of str, student names
        """
        failed_students = []
        # Iterate through students to find those with failing scores
        for name, info in self.students.items():
            if any(score < 60 for score in info['courses'].values()):
                failed_students.append(name)
        return failed_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average score of this course or None if no records
        """
        total_score = 0
        count = 0
        # Iterate through students to calculate the course average
        for info in self.students.values():
            if course in info['courses']:
                total_score += info['courses'][course]
                count += 1
        if count > 0:
            return total_score / count
        return None

    def get_top_student(self):
        """
        Calculate every student's GPA with get_gpa method, and find the student with the highest GPA.
        :return: str, name of student whose GPA is highest
        """
        top_student = None
        highest_gpa = 0
        # Iterate through students to find the top student
        for name in self.students:
            gpa = self.get_gpa(name)
            if gpa is not None and gpa > highest_gpa:
                highest_gpa = gpa
                top_student = name
        return top_student