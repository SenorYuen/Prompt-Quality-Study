class AssessmentSystem:
    """
    This is a class as an student assessment system, which supports add student, add course score, calculate GPA, and other functions for students and courses.
    """

    def __init__(self):
        """
        Initialize the students dict in assessment system.
        """
        # Initialize an empty dictionary to store student information
        self.students = {}

    def add_student(self, name, grade, major):
        """
        Add a new student into self.students dict
        :param name: str, student name
        :param grade: int, student grade
        :param major: str, student major
        """
        # Create a new dictionary for the student with name, grade, major, and an empty courses dictionary
        self.students[name] = {'name': name, 'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        """
        Add score of specific course for student in self.students
        :param name: str, student name
        :param course: str, course name
        :param score: int, course score
        """
        # Check if the student exists in the system
        if name in self.students:
            # Add the course score to the student's courses dictionary
            self.students[name]['courses'][course] = score

    def get_gpa(self, name):
        """
        Get average grade of one student.
        :param name: str, student name
        :return: if name is in students and this students have courses grade, return average grade(float)
                    or None otherwise
        """
        # Check if the student exists in the system and has courses
        if name in self.students and self.students[name]['courses']:
            # Calculate the average grade
            average_grade = sum(self.students[name]['courses'].values()) / len(self.students[name]['courses'])
            return average_grade
        else:
            return None

    def get_all_students_with_fail_course(self):
        """
        Get all students who have any score below 60
        :return: list of str, student name
        """
        # Initialize an empty list to store students with failed courses
        failed_students = []
        # Iterate over each student in the system
        for student in self.students:
            # Iterate over each course the student has
            for course, score in self.students[student]['courses'].items():
                # Check if the score is below 60
                if score < 60:
                    # Add the student to the list of failed students
                    failed_students.append(student)
                    # Break out of the loop to avoid adding the same student multiple times
                    break
        return failed_students

    def get_course_average(self, course):
        """
        Get the average score of a specific course.
        :param course: str, course name
        :return: float, average scores of this course if anyone have score of this course, or None if nobody have records.
        """
        # Initialize a list to store scores for the course
        course_scores = []
        # Iterate over each student in the system
        for student in self.students:
            # Check if the student has the course
            if course in self.students[student]['courses']:
                # Add the score to the list of course scores
                course_scores.append(self.students[student]['courses'][course])
        # Check if there are any scores for the course
        if course_scores:
            # Calculate and return the average score
            return sum(course_scores) / len(course_scores)
        else:
            return None

    def get_top_student(self):
        """
        Calculate every student's gpa with get_gpa method, and find the student with highest gpa
        :return: str, name of student whose gpa is highest
        """
        # Initialize the top student and their GPA
        top_student = None
        top_gpa = 0
        # Iterate over each student in the system
        for student in self.students:
            # Calculate the student's GPA
            gpa = self.get_gpa(student)
            # Check if the GPA is not None and is higher than the current top GPA
            if gpa is not None and gpa > top_gpa:
                # Update the top student and their GPA
                top_student = student
                top_gpa = gpa
        return top_student