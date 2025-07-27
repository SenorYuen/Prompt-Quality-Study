class ClassRegistrationSystem:
    def __init__(self):
        self.students = []
        self.students_registration_classes = {}

    def register_student(self, student):
        if student in self.students:
            return 0
        else:
            self.students.append(student)
            self.students_registration_classes[student["name"]] = []
            return 1

    def register_class(self, student_name, class_name):
        if student_name in self.students_registration_classes:
            self.students_registration_classes[student_name].append(class_name)
            return self.students_registration_classes[student_name]
        return []

    def get_students_by_major(self, major):
        return [student["name"] for student in self.students if student["major"] == major]

    def get_all_major(self):
        return list(set(student["major"] for student in self.students))

    def get_most_popular_class_in_major(self, major):
        class_count = {}
        for student in self.students:
            if student["major"] == major:
                for class_name in self.students_registration_classes[student["name"]]:
                    if class_name in class_count:
                        class_count[class_name] += 1
                    else:
                        class_count[class_name] = 1
        if class_count:
            return max(class_count, key=class_count.get)
        return None