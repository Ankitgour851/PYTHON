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


class Programmer(Employee):
    def __init__(self, fname, lname, salary,proglang,exp):
        super().__init__(fname, lname, salary)
        self.proglang=proglang
        self.exp=exp

    def increase(self):
        self.salary=int(self.salary*(self.increment+0.2))
        # return self.salary
        # return 'thenga'

harry=Programmer('harry','jackson',99000,'python','5 yrs')
# print(harry.exp)
# print(help(Programmer))
# help(Programmer)
print(harry.increase())