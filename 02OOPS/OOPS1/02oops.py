class Employee:
#class variable
    increment=1.5
    no_of_employeess=0

    #Constructor
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        self.increment=1.4
        Employee.no_of_employeess+=1

    def increase(self):
        # self.salary=int(self.salary * Employee.increment)
        self.salary=int(self.salary * self.increment)


print(Employee.no_of_employeess)
harry=Employee('harry','jackson',4400)
print(Employee.no_of_employeess)
rohan=Employee('rohan','das',4400)
print(Employee.no_of_employeess)


# print(harry.salary)
# print(harry.__dict__)
# harry.increment=9
# harry.increase()
# print(harry.salary)
# print(harry.__dict__)
# print(Employee.__dict__)
