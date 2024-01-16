class Person:
    def __init__(self,firstname,lastname,age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        
    def print_name(self):
        print(f"Hello! My name is {self.firstname} {self.lastname}. I am {self.age} years old.")
        
        
class Student(Person):
    def __init__(self,firstname, lastname, age, gender):
        super().__init__(firstname,lastname, age)
        self.gender = gender
        
    def print_name(self):
        print(f"Hello! My name is {self.firstname} {self.lastname}." + 
              f"I am {self.age} years old. I am a {self.gender}.")

if __name__ == '__main__':
    cls = Student("John", "Mendis",25,'Male')
    cls.print_name()