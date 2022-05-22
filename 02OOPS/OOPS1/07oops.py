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

    @staticmethod
    def isopen(day):
        if day=="sunday":
            return False
        else:
            return True
        

#  Magic_Dunder Methods
    def __add__(self,other):
        return self.salary+other.salary

    def __repr__(self):
        return f"Employee('{self.fname},{self.lname},{self.salary}')"

    def __str__(self):
        return f"Employee name is {self.fname}"


harry=Employee('harry','jackson',99000)
rohan=Employee('rohan','das',9)

# a=6
# print(a.__add__(7))
# print(a.__mul__(7))

# print(harry+rohan)
print(repr(harry))
print(str(harry))