class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.fullname = lastname
        self.email = firstname.lower() + "." + lastname.lower() + "@company.com"
    # Complete the code!


emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary", "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.email)
