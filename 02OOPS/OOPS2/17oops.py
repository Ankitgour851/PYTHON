class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"

    # def email(self):
    #     return f"{self.fname}.{self.lname}@codewithharry.com"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set,Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self,string):
        print("Setting.Now.....")
        names=string.split("@")[0]
        self.fname=string.split(".")[0]
        self.lname=string.split(".")[1]
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

skillf=Employee("Skill","F")
# print(skillf.email)

# print(type(skillf))
# print(id("this is string"))

o="this is string"
# print(dir(o))
# print(dir(skillf))

import inspect
print(inspect.getmembers(skillf))




