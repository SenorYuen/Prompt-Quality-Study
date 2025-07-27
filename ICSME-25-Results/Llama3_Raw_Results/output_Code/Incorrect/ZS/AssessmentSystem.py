class AssessmentSystem:
    def __init__(self):
        # Initialize an empty dictionary to store students' information
        self.students = {}

    def add_student(self, name, grade, major):
        # Add a new student into the dictionary with an empty dictionary for courses
        self.students[name] = {'grade': grade, 'major': major, 'courses': {}}

    def add_course_score(self, name, course, score):
        # Check if the student exists in the system
        if name in self.students:
            # Add the course score to the student's courses dictionary
            self.students[name]['courses'][course] = score
        else:
            # Raise an error if the student does not exist
            raise ValueError("Student does not exist in the system")

    def get_gpa(self, name):
        # Check if the student exists in the system
        if name in self.students:
            # Get the student's courses dictionary
            courses = self.students[name]['courses']
            # Check if the student has any courses
            if courses:
                # Calculate the average grade
                gpa = sum(courses.values()) / len(courses)
                return gpa
            else:
                # Return None if the student has no courses
                return None
        else:
            # Return None if the student does not exist
            return None

    def get_all_students_with_fail_course(self):
        # Initialize an empty list to store students with failing courses
        failing_students = []
        # Iterate over each student in the system
        for name, student in self.students.items():
            # Iterate over each course the student is taking
            for course, score in student['courses'].items():
                # Check if the student has a failing grade in the course
                if score < 60:
                    # Add the student to the list of failing students
                    failing_students.append(name)
                    # Break out of the loop to avoid adding the same student multiple times
                    break
        # Return the list of failing students
        return failing_students

    def get_course_average(self, course):
        # Initialize variables to store the sum of scores and the count of students
        total_score = 0
        student_count = 0
        # Iterate over each student in the system
        for student in self.students.values():
            # Check if the student is taking the course
            if course in student['courses']:
                # Add the student's score to the total score
                total_score += student['courses'][course]
                # Increment the student count
                student_count += 1
        # Check if any students are taking the course
        if student_count > 0:
            # Calculate and return the average score
            return total_score / student_count
        else:
            # Return None if no students are taking the course
            return None

    def get_top_student(self):
        # Initialize variables to store the top student and their GPA
        top_student = None
        top_gpa = 0
        # Iterate over each student in the system
        for name, student in self.students.items():
            # Calculate the student's GPA
            gpa = self.get_gpa(name)
            # Check if the student's GPA is higher than the current top GPA
            if gpa is not None and gpa > top_gpa:
                # Update the top student and GPA
                top_student = name
                top_gpa = gpa
        # Return the top student
        return top_student