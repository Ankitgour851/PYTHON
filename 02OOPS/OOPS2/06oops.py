class Employee:
    no_of_leaves=8

    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    
    def printdetails(self):
        return f"Name is {self.name}.Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_str(cls,string):
     return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is Good " + string)

harry =Employee("Harry",455,"Instructor")
rohan =Employee("Rohan",420,"Sudent")
karan=Employee.from_str("Karan-480-Student")
harry.change_leaves(34)

karan.printgood("Harry")
Employee.printgood("Hanuman")