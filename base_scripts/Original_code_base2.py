
def print_hello_there():
    print("Hello There, World!")

def print_goodbye():
    print("Goodbye World!")

class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
        
    def get_salary_increase(self, percentage):
        self.salary = self.salary + (self.salary * percentage / 100)

