def add1(x,y):
    return x + y


print("From app.py buddy:", add1(2, 3))


def div1(x1, y1):
    if y1 <= 0:
        raise ValueError("Denominators must be greater than zero")
    return x1 / y1


class Company:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee, name):
        if employee in self.employees:
            raise ValueError("Employee with this ID already exists")
        self.employees[employee] = name

    def get_employee(self, employee_id):
        if employee_id not in self.employees:
            raise ValueError("Employee with this ID does not exist")
        return self.employees[employee_id]

    def delete_employee(self, employee_id):
        if employee_id not in self.employees:
            raise ValueError("Employee with this ID does not exist")
        del self.employees[employee_id]


print("Completed app.py")
