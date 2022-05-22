# Public
# Protected       _startwith
# private         __startwith


class Employee:
    no_of_leaves=8
    var=8
    _protected=9
    __private=88

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

har=Employee("Harry",343,"Student")
print(har._protected)
print(har._Employee__private)