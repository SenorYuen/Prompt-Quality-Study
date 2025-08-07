from datetime import datetime

class Classroom:
    def __init__(self, id):
        """
        Initialize the classroom management system.
        """
        self.id = id
        # Initialize an empty list to store the courses scheduled in this classroom
        self.courses = []

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        """
        # Check if the course is not already in the list
        if course not in self.courses:
            # Add the course to the list
            self.courses.append(course)

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
        Check if the classroom is free at the given time.
        :param check_time: Time to check in '%H:%M' format.
        :return: True if the check_time does not conflict with any course time, or False otherwise.
        """
        # Convert check_time to datetime object for comparison
        check_time = datetime.strptime(check_time, '%H:%M').time()
        
        # Iterate through the courses to check for time conflicts
        for course in self.courses:
            # Assuming each course has 'start_time' and 'end_time' attributes
            start_time = datetime.strptime(course['start_time'], '%H:%M').time()
            end_time = datetime.strptime(course['end_time'], '%H:%M').time()
            
            # Check if the check_time falls within the course time
            if start_time <= check_time < end_time:
                return False
        
        # Return True if no conflict is found
        return True

    def check_course_conflict(self, new_course):
        """
        Check if the new course time conflicts with any other course.
        :param new_course: A dictionary with 'start_time' and 'end_time' in '%H:%M' format.
        :return: False if the new course time conflicts with other courses, or True otherwise.
        """
        # Convert new course times to datetime objects for comparison
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M').time()
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M').time()
        
        # Iterate through the existing courses to check for time conflicts
        for course in self.courses:
            # Assuming each course has 'start_time' and 'end_time' attributes
            start_time = datetime.strptime(course['start_time'], '%H:%M').time()
            end_time = datetime.strptime(course['end_time'], '%H:%M').time()
            
            # Check for overlap in course times
            if (new_start_time < end_time and new_end_time > start_time):
                return False
        
        # Return True if no conflict is found
        return True