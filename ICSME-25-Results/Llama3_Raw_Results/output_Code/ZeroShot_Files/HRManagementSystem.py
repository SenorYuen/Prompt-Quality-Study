class HRManagementSystem:
    def __init__(self):
        # Initialize the HRManagementSystem with an attribute employees, which is an empty dictionary.
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        # Check if the employee is already in the HRManagementSystem.
        if employee_id in self.employees:
            # If the employee is already in the HRManagementSystem, return False.
            return False
        else:
            # If the employee is not in the HRManagementSystem, add the employee and return True.
            self.employees[employee_id] = {
                "name": name,
                "position": position,
                "department": department,
                "salary": salary
            }
            return True

    def remove_employee(self, employee_id):
        # Check if the employee is already in the HRManagementSystem.
        if employee_id in self.employees:
            # If the employee is in the HRManagementSystem, remove the employee and return True.
            del self.employees[employee_id]
            return True
        else:
            # If the employee is not in the HRManagementSystem, return False.
            return False

    def update_employee(self, employee_id: int, employee_info: dict):
        # Check if the employee is already in the HRManagementSystem.
        if employee_id in self.employees:
            # If the employee is in the HRManagementSystem, update the employee's information and return True.
            self.employees[employee_id].update(employee_info)
            return True
        else:
            # If the employee is not in the HRManagementSystem, return False.
            return False

    def get_employee(self, employee_id):
        # Check if the employee is already in the HRManagementSystem.
        if employee_id in self.employees:
            # If the employee is in the HRManagementSystem, return the employee's information.
            return self.employees[employee_id]
        else:
            # If the employee is not in the HRManagementSystem, return False.
            return False

    def list_employees(self):
        # Return a list of all employees' information.
        return list(self.employees.values())

# Example usage:
if __name__ == "__main__":
    hr_system = HRManagementSystem()
    print(hr_system.add_employee(1, "John Doe", "Software Engineer", "IT", 50000))  # True
    print(hr_system.add_employee(1, "Jane Doe", "Data Scientist", "Data", 60000))  # False
    print(hr_system.get_employee(1))  # {'name': 'John Doe', 'position': 'Software Engineer', 'department': 'IT', 'salary': 50000}
    print(hr_system.update_employee(1, {"position": "Senior Software Engineer"}))  # True
    print(hr_system.get_employee(1))  # {'name': 'John Doe', 'position': 'Senior Software Engineer', 'department': 'IT', 'salary': 50000}
    print(hr_system.remove_employee(1))  # True
    print(hr_system.get_employee(1))  # False
    print(hr_system.list_employees())  # []