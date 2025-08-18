'''
# This is a class representing a classroom, capable of adding and removing courses, checking availability at a given time, and detecting conflicts when scheduling new courses.

from datetime import datetime

class Classroom:
    def __init__(self, id):
        """
        Initialize the classroom management system.
        """

    def add_course(self, course):
        """
        Add course to self.courses list if the course wasn't in it.
        """

    def remove_course(self, course):
        """
        Remove course from self.courses list if the course was in it.
        """

    def is_free_at(self, check_time):
        """
        change the time format as '%H:%M' and check the time is free or not in the classroom.
        :return: True if the check_time does not conflict with every course time, or False otherwise.
        """

    def check_course_conflict(self, new_course):
        """
        Before adding a new course, check if the new course time conflicts with any other course.
        :return: False if the new course time conflicts(including two courses have the same boundary time) with other courses, or True otherwise.
        """

'''

from datetime import datetime


class Classroom:
    def __init__(self, id):
        self.id = id
        self.courses = []

    def add_course(self, course):

        if course not in self.courses:
            self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def is_free_at(self, check_time):
        check_time = datetime.strptime(check_time, '%H:%M')

        for course in self.courses:
            if datetime.strptime(course['start_time'], '%H:%M') <= check_time <= datetime.strptime(course['end_time'],
                                                                                                   '%H:%M'):
                return False
        return True

    def check_course_conflict(self, new_course):
        new_start_time = datetime.strptime(new_course['start_time'], '%H:%M')
        new_end_time = datetime.strptime(new_course['end_time'], '%H:%M')

        flag = True
        for course in self.courses:
            start_time = datetime.strptime(course['start_time'], '%H:%M')
            end_time = datetime.strptime(course['end_time'], '%H:%M')
            if start_time <= new_start_time and end_time >= new_start_time:
                flag = False
            if start_time <= new_end_time and end_time >= new_end_time:
                flag = False
        return flag

