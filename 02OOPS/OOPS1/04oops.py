class Employee:
    increment=1.5

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.increment=2

    def increase(self):
        self.salary=int(self.salary*self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount

    @classmethod
    def from_str(cls,emp_string):
        fname,lname,salary=emp_string.split("-")
        return cls(fname,lname,salary)

harry=Employee("harry", "Ram", 44400)
lovish=Employee.from_str("lovish-jckson-76000")
rohan=Employee("rohan","das",74000)

print(lovish.salary)