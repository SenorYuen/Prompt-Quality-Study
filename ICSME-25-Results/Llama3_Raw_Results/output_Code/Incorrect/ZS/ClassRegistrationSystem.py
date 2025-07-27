class ClassRegistrationSystem:
    def __init__(self):
        # Initialize the registration system with the attribute students and students_registration_class.
        self.students = []  # list of student dictionaries
        self.students_registration_class = {}  # dictionary, key is the student name, value is a list of class names

    def register_student(self, student):
        # register a student to the system, add the student to the students list, if the student is already registered, return 0, else return 1
        if student in self.students:
            return 0  # student already registered
        else:
            self.students.append(student)
            self.students_registration_class[student['name']] = []  # initialize empty class list for the student
            return 1  # student registered successfully

    def register_class(self, student_name, class_name):
        # register a class to the student.
        if student_name in self.students_registration_class:
            self.students_registration_class[student_name].append(class_name)  # add class to the student's class list
        return self.students_registration_class[student_name]  # return a list of class names that the student has registered

    def get_students_by_major(self, major):
        # get all students in the major
        students_in_major = [student['name'] for student in self.students if student['major'] == major]
        return students_in_major  # return a list of student name

    def get_all_major(self):
        # get all majors in the system
        all_majors = list(set([student['major'] for student in self.students]))
        return all_majors  # return a list of majors

    def get_most_popular_class_in_major(self, major):
        # get the class with the highest enrollment in the major.
        students_in_major = self.get_students_by_major(major)
        class_enrollments = {}
        for student in students_in_major:
            classes = self.students_registration_class[student]
            for class_name in classes:
                if class_name in class_enrollments:
                    class_enrollments[class_name] += 1
                else:
                    class_enrollments[class_name] = 1
        if class_enrollments:
            most_popular_class = max(class_enrollments, key=class_enrollments.get)
            return most_popular_class  # return a string of the most popular class in this major
        else:
            return None  # return None if no classes are registered in the major


class Classroom:
    def __init__(self, class_name, capacity):
        # Initialize the classroom with the attribute class_name and capacity.
        self.class_name = class_name
        self.capacity = capacity
        self.enrolled_students = []  # list to keep track of enrolled students

    def enroll_student(self, student_name):
        # enroll a student in the class.
        if len(self.enrolled_students) < self.capacity:
            self.enrolled_students.append(student_name)
            return True  # student enrolled successfully
        else:
            return False  # class is full

    def get_enrolled_students(self):
        # get all students enrolled in the class.
        return self.enrolled_students  # return a list of student names

    def get_class_name(self):
        # get the name of the class.
        return self.class_name  # return a string of the class name

    def get_capacity(self):
        # get the capacity of the class.
        return self.capacity  # return an integer of the class capacity


# Example usage:
if __name__ == "__main__":
    registration_system = ClassRegistrationSystem()
    student1 = {'name': 'John', 'major': 'CS'}
    student2 = {'name': 'Alice', 'major': 'CS'}
    student3 = {'name': 'Bob', 'major': 'Math'}

    registration_system.register_student(student1)
    registration_system.register_student(student2)
    registration_system.register_student(student3)

    registration_system.register_class('John', 'Data Structures')
    registration_system.register_class('John', 'Algorithms')
    registration_system.register_class('Alice', 'Data Structures')
    registration_system.register_class('Bob', 'Linear Algebra')

    print(registration_system.get_students_by_major('CS'))  # Output: ['John', 'Alice']
    print(registration_system.get_all_major())  # Output: ['CS', 'Math']
    print(registration_system.get_most_popular_class_in_major('CS'))  # Output: 'Data Structures'

    classroom = Classroom('Data Structures', 10)
    print(classroom.enroll_student('John'))  # Output: True
    print(classroom.enroll_student('Alice'))  # Output: True
    print(classroom.get_enrolled_students())  # Output: ['John', 'Alice']
    print(classroom.get_class_name())  # Output: 'Data Structures'
    print(classroom.get_capacity())  # Output: 10