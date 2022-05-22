'''
lambda argument : manuplate(argument)
'''

# def add(a,b):
#     s=a+b
#     return s
add=lambda x,y:x+y
# add=lambda x,y:x>y

# print(add(4,6))

def x(val):
    return val[1]

a=[(1,2),(4,5),(555,3),(2,554)]
# a.sort(key=lambda x:x[1])
a.sort(key=x)
print(a)