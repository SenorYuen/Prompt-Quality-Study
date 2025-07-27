class HRManagementSystem:
    """
    This is a class as personnel management system that implements functions such as adding, deleting, querying, and updating employees
    """

    def __init__(self):
        """
        Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
        """
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        """
        Add a new employee to the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param name: The employee's name, str.
        :param position: The employee's position, str.
        :param department: The employee's department, str.
        :param salary: The employee's salary, int.
        :return: If the employee is already in the HRManagementSystem, returns False, otherwise, returns True.
        """
        # Check if the employee already exists
        if employee_id in self.employees:
            return False
        # Add the new employee to the dictionary
        self.employees[employee_id] = {
            'name': name,
            'position': position,
            'department': department,
            'salary': salary
        }
        return True

    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        # Check if the employee exists
        if employee_id in self.employees:
            # Remove the employee from the dictionary
            del self.employees[employee_id]
            return True
        return False

    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :param employee_info: The employee's information, dict.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        # Check if the employee exists
        if employee_id in self.employees:
            # Update the employee's information
            self.employees[employee_id] = employee_info
            return True
        return False

    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :param employee_id: The employee's id, int.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
        """
        # Check if the employee exists
        if employee_id in self.employees:
            # Return the employee's information
            return self.employees[employee_id]
        return False

    def list_employees(self):
        """
        List all employees' information in the HRManagementSystem.
        :return: A dictionary of all employees' information.
        """
        # Create a new dictionary to store the employee information with employee ID
        employees_list = {}
        for employee_id, employee_info in self.employees.items():
            # Add the employee ID to the employee information
            employee_info['employee_ID'] = employee_id
            # Add the employee information to the list
            employees_list[employee_id] = employee_info
        return employees_list