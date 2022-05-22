#  Map function

# map(function_to_apply,list of inputs)

def square(n):
    return n**2
h1=[1,2,3,4,5,7]

# sq=[]
# for item in h1:
#     sq.append(item**2)

sq =list(map(square, h1))
# print(sq)


# Filter function
def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

hf1=[1,2,3,4,5,-2,-4,-1,-55,77,-23,0,4,3,5,55,66,77]
greater_than_2 =list(filter(greater_than_2,hf1))
# print(greater_than_2)


# Reduce function
from functools import reduce

def sum_num(a,b):
    return a+b

li1=reduce(sum_num,[1,2,3,4])
print(li1)