class ClassRegistrationSystem:
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major, get a list of all majors, and determine the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionaries, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        """
        # Check if the student is already registered
        for existing_student in self.students:
            if existing_student["name"] == student["name"]:
                return 0
        # If not, add the student to the list and return 1
        self.students.append(student)
        return 1

    def register_class(self, student_name, class_name):
        """
        register a class to the student.
        :param student_name: str
        :param class_name: str
        :return a list of class names that the student has registered
        """
        # Check if the student is registered
        for student in self.students:
            if student["name"] == student_name:
                # If the student is registered, add the class to their list of classes
                if student_name in self.students_registration_classes:
                    self.students_registration_classes[student_name].append(class_name)
                else:
                    self.students_registration_classes[student_name] = [class_name]
                # Return the list of classes the student is registered for
                return self.students_registration_classes[student_name]
        # If the student is not registered, return an empty list
        return []

    def get_students_by_major(self, major):
        """
        get all students in the major
        :param major: str
        :return a list of student name
        """
        # Initialize an empty list to store the students in the major
        students_in_major = []
        # Iterate over the students
        for student in self.students:
            # Check if the student's major matches the given major
            if student["major"] == major:
                # If it does, add the student's name to the list
                students_in_major.append(student["name"])
        # Return the list of students in the major
        return students_in_major

    def get_all_major(self):
        """
        get all majors in the system
        :return a list of majors
        """
        # Initialize an empty set to store the majors (using a set to avoid duplicates)
        majors = set()
        # Iterate over the students
        for student in self.students:
            # Add the student's major to the set
            majors.add(student["major"])
        # Convert the set to a list and return it
        return list(majors)

    def get_most_popular_class_in_major(self, major):
        """
        get the class with the highest enrollment in the major.
        :return  a string of the most popular class in this major
        """
        # Initialize an empty dictionary to store the count of each class
        class_counts = {}
        # Iterate over the students in the major
        for student_name in self.get_students_by_major(major):
            # Get the classes the student is registered for
            classes = self.students_registration_classes.get(student_name, [])
            # Iterate over the classes
            for class_name in classes:
                # Increment the count for the class
                if class_name in class_counts:
                    class_counts[class_name] += 1
                else:
                    class_counts[class_name] = 1
        # Find the class with the highest count
        most_popular_class = max(class_counts, key=class_counts.get) if class_counts else None
        # Return the most popular class
        return most_popular_class