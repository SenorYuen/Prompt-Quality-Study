class HRManagementSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, position, department, salary):
        if employee_id in self.employees:
            return False
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
        return False

    def update_employee(self, employee_id, employee_info):
        if employee_id in self.employees:
            self.employees[employee_id].update(employee_info)
            return True
        return False

    def get_employee(self, employee_id):
        return self.employees.get(employee_id, False)

    def list_employees(self):
        return self.employees