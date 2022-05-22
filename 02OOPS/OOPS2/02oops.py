class Employee:
    no_of_leaves=8
    pass

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.salary=455
rohan.name="Rohan"
rohan.salary=420
# rohan.no_of_leaves=10

print(harry.name)
print(harry.salary)
print(harry.no_of_leaves)


print(rohan.name)
print(rohan.salary)
# print(rohan.no_of_leaves)


print(Employee.no_of_leaves)
print(Employee.__dict__)

Employee.no_of_leaves=9
print(Employee.__dict__)

# print(rohan.__dict__)
# rohan.no_of_leaves=9
# print(rohan.__dict__)

print(Employee.no_of_leaves)

