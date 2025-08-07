class ClassRegistrationSystem:
    def __init__(self):
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        for s in self.students:
            if s['name'] == student['name']:
                return 0
        self.students.append(student)
        return 1

    def register_class(self, student_name, class_name):
        if student_name not in self.students_registration_classes:
            self.students_registration_classes[student_name] = []
        if class_name not in self.students_registration_classes[student_name]:
            self.students_registration_classes[student_name].append(class_name)
        return self.students_registration_classes[student_name]

    def get_students_by_major(self, major):
        return [student['name'] for student in self.students if student['major'] == major]

    def get_all_majors(self):
        return list(set(student['major'] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        class_count = {}
        students_in_major = self.get_students_by_major(major)
        for student in students_in_major:
            if student in self.students_registration_classes:
                for class_name in self.students_registration_classes[student]:
                    if class_name in class_count:
                        class_count[class_name] += 1
                    else:
                        class_count[class_name] = 1
        if not class_count:
            return None
        return max(class_count, key=class_count.get)