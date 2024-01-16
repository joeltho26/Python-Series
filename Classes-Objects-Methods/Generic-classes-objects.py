class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
    def print_name(self):
        print(f"Hello! My name is {self.firstname} {self.lastname}. I am {self.age} years old.")
        
        
class Student(Person):
    pass

if __name__ == '__main__':
    cls = Student("John", "Mendis",25)
    cls.print_name()