from employee import Employee


class Manager(Employee):
    def __init__(self, first: str, last: str, pay: str, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("-->", emp.fullname)
