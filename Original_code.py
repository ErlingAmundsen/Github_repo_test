# CODE BLOCK A
x = 5
y = 10

# CODE BLOCK B
x = 7
z = 15

# CODE BLOCK C
y = 12
z = 15

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
        
def main():
    print("Hello World")
    print("Welcome to my Python program!")
    
    
if __name__ == "__main__":
    main()
    
