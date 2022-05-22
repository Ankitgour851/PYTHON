class Employee:
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary

    @property
    def email(self):
        return f'Harry email is {self.fname}{self.lname}@gmail.com'

    @email.setter
    def email(self,cng_email):
        cn_email=cng_email.split('.')
        self.fname=cn_email[0]
        self.lname=cn_email[1]

    def __add__(self,other):
        return self.salary+other.salary

harry=Employee("Harshita", "sarathe", 900)
# print(harry.email)
# harry.email="harry.bhai"
# print(harry.email)
print(harry.salary+4000)