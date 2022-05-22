class Employee:
#class variable
    increment=1.5
    no_of_employeess=0
#Constructor
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        Employee.no_of_employeess+=1
    
    def increase(self):
        self.salary=int(self.salary * self.increment)
    
# change the value of class employee
    @classmethod
    def change_increment(cls,amount):
        cls.increment=amount


harry=Employee('harry','jackson',4400)
rohan=Employee('rohan','das',4400)

print(harry.salary)
Employee.change_increment(3)
harry.increase()
print(harry.salary)
