from datetime import datetime

class Course:
    def __init__(self, name, start_time, end_time):
        """
        Initialize a course with name, start_time, and end_time.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

class Classroom:
    def __init__(self, id):
        """
        Initialize the classroom management system.
        """
        # Initialize an empty list to store courses
        self.courses = []
        # Initialize the classroom id
        self.id = id

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        """
        # Check if the course is not already in the list
        if course not in self.courses:
            # Check for conflicts before adding the course
            if self.check_course_conflict(course):
                # Add the course to the list if no conflicts
                self.courses.append(course)
            else:
                # Print a message if the course conflicts with existing courses
                print(f"Cannot add {course.name} due to time conflict.")

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        """
        # Check if the course is in the list
        if course in self.courses:
            # Remove the course from the list
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        Change the time format as '%H:%M' and check the time is free or not in the classroom.
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """
        # Convert check_time to datetime object if it's a string
        if isinstance(check_time, str):
            check_time = datetime.strptime(check_time, '%H:%M')
        # Iterate over each course in the classroom
        for course in self.courses:
            # Convert course start and end times to datetime objects if they're strings
            if isinstance(course.start_time, str):
                course_start_time = datetime.strptime(course.start_time, '%H:%M')
            else:
                course_start_time = course.start_time
            if isinstance(course.end_time, str):
                course_end_time = datetime.strptime(course.end_time, '%H:%M')
            else:
                course_end_time = course.end_time
            # Check if check_time is within a course time
            if course_start_time <= check_time < course_end_time:
                # Return False if check_time conflicts with a course
                return False
        # Return True if check_time does not conflict with any courses
        return True

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """
        # Iterate over each course in the classroom
        for course in self.courses:
            # Convert new course start and end times to datetime objects if they're strings
            if isinstance(new_course.start_time, str):
                new_start_time = datetime.strptime(new_course.start_time, '%H:%M')
            else:
                new_start_time = new_course.start_time
            if isinstance(new_course.end_time, str):
                new_end_time = datetime.strptime(new_course.end_time, '%H:%M')
            else:
                new_end_time = new_course.end_time
            # Convert course start and end times to datetime objects if they're strings
            if isinstance(course.start_time, str):
                course_start_time = datetime.strptime(course.start_time, '%H:%M')
            else:
                course_start_time = course.start_time
            if isinstance(course.end_time, str):
                course_end_time = datetime.strptime(course.end_time, '%H:%M')
            else:
                course_end_time = course.end_time
            # Check for conflicts between new course and existing course
            if (new_start_time < course_end_time and new_end_time > course_start_time) or \
               (new_start_time == course_start_time or new_end_time == course_end_time):
                # Return False if a conflict is found
                return False
        # Return True if no conflicts are found
        return True


# Example usage:
classroom = Classroom(1)
course1 = Course("Math", "09:00", "10:00")
course2 = Course("Science", "10:00", "11:00")
course3 = Course("English", "10:00", "11:00")

classroom.add_course(course1)
classroom.add_course(course2)
classroom.add_course(course3)

print(classroom.is_free_at("11:00"))  # Should print: True
print(classroom.is_free_at("10:00"))  # Should print: False