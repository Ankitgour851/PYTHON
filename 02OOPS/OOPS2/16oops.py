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


hindustani_supporter=Employee("Hindustani","Supporter")
# nikhil_raj_pandey=Employee("Nikil","Raj")

# print(hindustani_supporter.explain())

# print(hindustani_supporter.email())
print(hindustani_supporter.email)


hindustani_supporter.fname="US"
# print(hindustani_supporter.email())
print(hindustani_supporter.email)

hindustani_supporter.email="this.that@codewithharry.com"
print(hindustani_supporter.fname)
print(hindustani_supporter.lname)
print(hindustani_supporter.email)


del hindustani_supporter.email
print(hindustani_supporter.email)

hindustani_supporter.email="Harry.Perry@codewithharry.com"
print(hindustani_supporter.email)




