'''
# This is a class as personnel management system that implements functions such as adding, deleting, querying, and updating employees

class HRManagementSystem:
    def __init__(self):
        """
        Initialize the HRManagementSystem withan attribute employees, which is an empty dictionary.
        """

    def add_employee(self, employee_id, name, position, department, salary):
        """
        Add a new employee to the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns False, otherwise, returns True.
        """

    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """

    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """

    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
        """

    def list_employees(self):
        “”“
        List all employees' information in the HRManagementSystem.
        :return: A list of all employees' information,dict.
        """

'''

class HRManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {
                'name': name,
                'position': position,
                'department': department,
                'salary': salary
            }
            return True

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False

    def update_employee(self, employee_id: int, employee_info: dict):
        employee = self.get_employee(employee_id)
        if employee == False:
            return False
        else:
            for key, value in employee_info.items():
                if key not in employee:
                    return False
            for key, value in employee_info.items():
                employee[key] = value
            return True

    def get_employee(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False

    def list_employees(self):
        employee_data = {}
        if self.employees:
            for employee_id, employee_info in self.employees.items():
                employee_details = {}
                employee_details["employee_ID"] = employee_id
                for key, value in employee_info.items():
                    employee_details[key] = value
                employee_data[employee_id] = employee_details
        return employee_data