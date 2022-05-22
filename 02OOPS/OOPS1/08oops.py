class Employee:
    increment=1.5

    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        # self.email=fname + lname +'@email.com'
        # self.increment=2

    def increase(self):
        self.salary=int(self.salary*self.increment)

    @property
    def email(self):
        if self.fname==None:
            return 'email not set'
        else:
            return self.fname + '.' + self.lname +'@email.com'

    @email.setter
    def email(self,given_email):
        name_list=given_email.split('@')[0]
        self.fname=given_email.split('.')[0]
        self.lname=given_email.split('.')[1]

    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None

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

if __name__ == '__main__':
    harry=Employee('harry','jackson',99000)
    rohan=Employee('rohan','das',9)
    # print(harry.email)
    # print(rohan.email)


    rohan.lname='Khanna'
    print(rohan.email)


    rohan.email='khana.rohan@gmail.com'
    print(rohan.email)


    del rohan.email
    print(rohan.email)