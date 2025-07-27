from datetime import datetime

class Classroom:
    """
    This is a class representing a classroom, capable of adding and removing courses, checking availability at a given time, and detecting conflicts when scheduling new courses.
    """

    def __init__(self, id):
        """
        Initialize the classroom management system.
        :param id: int, the id of classroom
        """
        self.id = id
        self.courses = []

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
        # Check if the course already exists in the list
        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        :param course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        """
        # Check if the course exists in the list
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :param check_time: str, the time need to be checked
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.is_free_at('10:00')
        True
        >>> classroom.is_free_at('9:00')
        False
        """
        # Convert check_time to minutes
        check_time_minutes = self.time_to_minutes(check_time)
        
        # Check each course in the classroom
        for course in self.courses:
            # Convert course times to minutes
            start_time_minutes = self.time_to_minutes(course['start_time'])
            end_time_minutes = self.time_to_minutes(course['end_time'])
            
            # Check if check_time is within a course time
            if start_time_minutes <= check_time_minutes < end_time_minutes:
                return False
        
        # If no conflicts are found, return True
        return True

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :param new_course: dict, information of the course, including 'start_time', 'end_time' and 'name'
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        >>> classroom = Classroom(1)
        >>> classroom.add_course({'name': 'math', 'start_time': '8:00', 'end_time': '9:40'})
        >>> classroom.check_course_conflict({'name': 'SE', 'start_time': '9:40', 'end_time': '10:40'})
        False
        """
        # Convert new course times to minutes
        new_start_time_minutes = self.time_to_minutes(new_course['start_time'])
        new_end_time_minutes = self.time_to_minutes(new_course['end_time'])
        
        # Check each course in the classroom
        for course in self.courses:
            # Convert course times to minutes
            start_time_minutes = self.time_to_minutes(course['start_time'])
            end_time_minutes = self.time_to_minutes(course['end_time'])
            
            # Check if new course time conflicts with a course time
            if (new_start_time_minutes < end_time_minutes and new_end_time_minutes > start_time_minutes) or \
               (new_start_time_minutes == start_time_minutes) or (new_end_time_minutes == end_time_minutes):
                return False
        
        # If no conflicts are found, return True
        return True

    def time_to_minutes(self, time_str):
        """
        Convert time string to minutes.
        :param time_str: str, time in 'HH:MM' format
        :return: int, time in minutes
        """
        # Split time string into hours and minutes
        hours, minutes = map(int, time_str.split(':'))
        
        # Convert time to minutes
        return hours * 60 + minutes