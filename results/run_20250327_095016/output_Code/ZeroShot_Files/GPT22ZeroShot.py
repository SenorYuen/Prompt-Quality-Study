class ClassRegistrationSystem:

    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionary, key is the student name, value is a list of class names
        """
        self.students = []  # List to store student dictionaries
        self.students_registration_class = {}  # Dictionary to store class registrations for each student

    def register_student(self, student):
        """
        Register a student to the system, add the student to the students list.
        If the student is already registered, return 0, else return 1.
        """
        # Check if the student is already registered
        for s in self.students:
            if s['name'] == student['name']:
                return 0
        # Add the student to the list
        self.students.append(student)
        # Initialize the student's class registration list
        self.students_registration_class[student['name']] = []
        return 1

    def register_class(self, student_name, class_name):
        """
        Register a class to the student.
        :return a list of class names that the student has registered
        """
        # Check if the student is registered
        if student_name in self.students_registration_class:
            # Add the class to the student's list if not already registered
            if class_name not in self.students_registration_class[student_name]:
                self.students_registration_class[student_name].append(class_name)
            return self.students_registration_class[student_name]
        else:
            # If the student is not found, return an empty list
            return []

    def get_students_by_major(self, major):
        """
        Get all students in the major.
        :return a list of student names
        """
        # List comprehension to filter students by major
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        Get all majors in the system.
        :return a list of majors
        """
        # Use a set to store unique majors
        majors = set(student['major'] for student in self.students)
        return list(majors)

    def get_most_popular_class_in_major(self, major):
        """
        Get the class with the highest enrollment in the major.
        :return a string of the most popular class in this major
        """
        # Dictionary to count class enrollments
        class_count = {}
        # Iterate over students in the specified major
        for student in self.students:
            if student['major'] == major:
                for class_name in self.students_registration_class.get(student['name'], []):
                    if class_name in class_count:
                        class_count[class_name] += 1
                    else:
                        class_count[class_name] = 1
        # Find the class with the maximum count
        if class_count:
            most_popular_class = max(class_count, key=class_count.get)
            return most_popular_class
        else:
            return None