class Department():

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.employees = []

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)


class Employee():

    def __init__(self, first_name, last_name, salary, department, middle_name = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary
        self.department = department
        self.department.add_employee(self)

    def full_name(self):
        if self.middle_name == None:
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.first_name} {self.middle_name} {self.last_name}"

    def change_salary(self, percent_increase):
        
        if percent_increase > 10:
            return None

        new_salary = self.salary * (1 + (.01 * percent_increase))

        if not new_salary < 40000:
            self.salary = new_salary

    def __repr__(self):
        return f"{self.first_name[0]}. {self.last_name}"


department_a = Department("Sales", "804A")
department_b = Department("Engineering", "201B")

employee_1 = Employee("Alex", "Smith", 82000, department_a)
employee_2 = Employee("Bradley", "Jones", 79000, department_a)
employee_3 = Employee("Charlie", "Adams", 65000, department_b)
employee_4 = Employee("Darla", "Smith", 85000, department_a, middle_name = "Allison")
employee_5 = Employee("Eric", "Smith", 40000, department_b)

print(employee_1)
print(department_a.employees)

