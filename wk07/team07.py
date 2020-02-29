"""
File: ta07-solution.py
Author: Br. Burton
Demonstrates inheritance and polymorphism.
"""
from abc import abstractmethod 

class Employee:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
            
    @abstractmethod
    def get_paycheck(self):
        pass

class HourlyEmployee(Employee):
    """
    An HourlyEmployee has an hourly wage.
    """
    def __init__(self, name, wage, hours):
        super().__init__(name)

        self.hourly_wage = wage
        self.hours = hours
    
    def get_paycheck(self):
        return self.hourly_wage * self.hours
        

    def display(self):
        print("{} - ${}/hour - Paycheck: {}".format(self.name, self.hourly_wage, self.get_paycheck()))

class SalaryEmployee(Employee):
    """
    A SalaryEmployee has a salary.
    """
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
        
    def get_paycheck(self):
        return self.salary // 52
       

    def display(self):
        print("{} - ${}/year - Paycheck: ${}".format(self.name, self.salary, self.get_paycheck()))

def main():
    """
    Prompt the user for a series of employees and then display
    their information at the end.
    """
    employees = []

    command = ""

    while command != "q":
        command = input("Enter 'h' (hourly employee), 's', (salary employee) or 'q': ")

        if command == "h":
            name = input("Enter name: ")
            wage = int(input("Enter wage: "))
            hours = int(input("Enter hours: "))
            emp = HourlyEmployee(name, wage, hours)
            employees.append(emp)
        elif command == "s":
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))
            emp = SalaryEmployee(name, salary)
            employees.append(emp)

    # We are done entering data, print them out now

    for employee in employees:
        employee.display()

if __name__ == "__main__":
    main()