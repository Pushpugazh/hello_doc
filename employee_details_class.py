# employee details using class
class Employee:  # class name with initial letter caps

    raise_amount = 1.04
    no_of_emp = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@company.com'

        Employee.no_of_emp += 1

    def fullname(self):
        return self.first + self.last

    def pay_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # runtime error
        # self.amount can be replaced by Employee.amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


emp_1 = Employee('Mark', 'Antony', 15000)
emp_2 = Employee('Manick', 'Basha', 12000)

print('Employee 1 - First name: ', emp_1.first)
print('Employee 2 - First name: ', emp_2.first)

print('Employee 1 - Full name: ', emp_1.fullname())
print('Employee 1 - Pay: ', emp_1.pay)

emp_1.pay_raise()  # calling the function pay raise.

print('Employee 1 - Pay after raise: ', emp_1.pay)
print('No of employees', Employee.no_of_emp)

new_emp_1 = 'John-mathiv-6000'
new_emp_2 = 'Jerin-ducklos-6500'

employee_1 = Employee.from_string(new_emp_1)
employee_2 = Employee.from_string(new_emp_2)

print('Employee 1(using string input) - email: ', employee_1.email )
