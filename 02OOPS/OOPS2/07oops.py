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

class Programmer(Employee):
    no_of_holiday=56
    def __init__(self, aname, asalary, arole,languages):
        # super().__init__(aname, asalary, arole)
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages

    def printprog(self):
        return f"Name of Programmer is {self.name}.Salary is {self.salary} and role is {self.role} and the languages are {self.languages}"


harry =Employee("Harry",455,"Instructor")
rohan =Employee("Rohan",420,"Sudent")

shubham=Programmer("Shubham",888,"Programmer",["Python","Cpp"])
karan=Programmer("Karan",988,"Programmer",["Python",'Cpp'])

print(karan.printprog(),karan.no_of_holiday)

