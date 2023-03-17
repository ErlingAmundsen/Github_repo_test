def print_hello():
    print("Hello World!")

def print_goodbye():
    print("Goodbye World!")

class Employee:
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
    def display_employee(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
        
    def add_experience(self, years):
        self.experience += years