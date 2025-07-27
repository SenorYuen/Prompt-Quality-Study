class HRManagementSystem:
    def __init__(self):
        """
        Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
        """
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        """
        Add a new employee to the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns False, otherwise, returns True.
        """
        if employee_id in self.employees:
            return False  # Employee already exists
        self.employees[employee_id] = {
            'name': name,
            'position': position,
            'department': department,
            'salary': salary
        }
        return True  # Employee added successfully

    def remove_employee(self, employee_id):
        """
        Remove an employee from the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True  # Employee removed successfully
        return False  # Employee not found

    def update_employee(self, employee_id: int, employee_info: dict):
        """
        Update an employee's information in the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns True, otherwise, returns False.
        """
        if employee_id in self.employees:
            self.employees[employee_id].update(employee_info)
            return True  # Employee information updated successfully
        return False  # Employee not found

    def get_employee(self, employee_id):
        """
        Get an employee's information from the HRManagementSystem.
        :return: If the employee is already in the HRManagementSystem, returns the employee's information, otherwise, returns False.
        """
        return self.employees.get(employee_id, False)

    def list_employees(self):
        """
        List all employees' information in the HRManagementSystem.
        :return: A list of all employees' information, dict.
        """
        return list(self.employees.values())