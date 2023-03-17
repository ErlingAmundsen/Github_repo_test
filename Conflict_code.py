# CODE BLOCK A
x = 5
y = 10

# CODE BLOCK B
x = 5
z = 15

# CODE BLOCK C
y = 10
z = 15


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
        

def main():
    print("Greetings Earthlings!")
    print("Hello World")
    
