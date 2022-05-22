class Employee:
    no_of_leaves=8
    var=8

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

class Player:
    no_of_Games=4
    var=14
    def __init__(self,name,game):
        self.name=name
        self.game=game
        
    def printdetails(self):
        return f"Name is {self.name}.Game is {self.game}"

class CoolProgrammer(Player,Employee):
    # var=10
    languages="C++"
    def printlanguages(self):
        print(self.languages)

harry =Employee("Harry",455,"Instructor")
rohan =Employee("Rohan",420,"Sudent")

shubham=Player("Shubham",["Cricket"])
karan=CoolProgrammer("Karan","Coolprogrammer")
det=karan.printdetails()
# karan.printlanguages()
# print(det)
print(karan.var)