class Employee:
    #Constructor
    def __init__(self,fname,lname,salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary


harry=Employee('harry','jackson',4400)
rohan=Employee('rohan','das',4400)

# harry.fname="harry"
# harry.lname="jackson"
# harry.salary=44000

# rohan.fname="rohan"
# rohan.lname="das"
# rohan.salary="44000"

print(harry.fname,rohan.fname)