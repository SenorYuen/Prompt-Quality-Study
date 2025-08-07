class ClassRegistrationSystem:
    """
    This is a class as a class registration system, allowing to register students, register them for classes, retrieve students by major, get a list of all majors, and determine the most popular class within a specific major.
    """

    def __init__(self):
        """
        Initialize the registration system with the attribute students and students_registration_class.
        students is a list of student dictionaries, each student dictionary has the key of name and major.
        students_registration_class is a dictionary, key is the student name, value is a list of class names
        """
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        """
        Register a student to the system, add the student to the students list.
        If the student is already registered, return 0, else return 1.
        """
        for s in self.students:
            if s['name'] == student['name']:
                return 0
        self.students.append(student)
        self.students_registration_classes[student['name']] = []
        return 1

    def register_class(self, student_name, class_name):
        """
        Register a class to the student.
        :param student_name: str
        :param class_name: str
        :return: a list of class names that the student has registered
        """
        if student_name in self.students_registration_classes:
            if class_name not in self.students_registration_classes[student_name]:
                self.students_registration_classes[student_name].append(class_name)
            return self.students_registration_classes[student_name]
        return []

    def get_students_by_major(self, major):
        """
        Get all students in the major.
        :param major: str
        :return: a list of student names
        """
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_major(self):
        """
        Get all majors in the system.
        :return: a list of majors
        """
        return list(set(student['major'] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        """
        Get the class with the highest enrollment in the major.
        :param major: str
        :return: a string of the most popular class in this major
        """
        class_count = {}
        for student in self.students:
            if student['major'] == major:
                student_classes = self.students_registration_classes.get(student['name'], [])
                for class_name in student_classes:
                    if class_name in class_count:
                        class_count[class_name] += 1
                    else:
                        class_count[class_name] = 1
        if class_count:
            return max(class_count, key=class_count.get)
        return None