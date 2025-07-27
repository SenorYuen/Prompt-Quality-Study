class HRManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id in self.employees:
            return False
        else:
            self.employees[employee_id] = {'name': name, 'position': position, 'department': department, 'salary': salary}
            return True

    def remove_employee(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        else:
            return False

    def update_employee(self, employee_id, employee_info):
        if employee_id in self.employees:
            self.employees[employee_id] = employee_info
            return True
        else:
            return False

    def get_employee(self, employee_id):
        if employee_id in self.employees:
            return self.employees[employee_id]
        else:
            return False

    def list_employees(self):
        result = {}
        for employee_id, employee_info in self.employees.items():
            result[employee_id] = {'employee_ID': employee_id, 'name': employee_info['name'], 'position': employee_info['position'], 'department': employee_info['department'], 'salary': employee_info['salary']}
        return result