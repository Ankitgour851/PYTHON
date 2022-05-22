'''
List comprehensions 
dictionary comprehensions
set comprehensions
generator comprehensions 

'''

list_1=[1,2,44,3,2,4,6,3,57,74,66,34,1,34,52,43,45,12,52,3,4,63]
div_by_3=[]
for item in list_1:
    if item%3==0:
        div_by_3.append(item)

# print("without using list comprehensions",div_by_3)
# print("by using list comprehension",[item for item in list_1 if item%3==0])


dict1={'a':45,'b':65,'A':5,'B':5}
# print({k.lower():dict1.get(k.lower(),0)+dict1.get(k.upper(),0) for k in dict1.keys()})


squared = {x**2 for x in [1,2,3,4,4,4,5,5,5,5,5]}
# print(squared)


gene = (i for i in range(56) if i%3==0)
print(gene)
# print(gene.__next__())
# print(gene.__next__())
# print(gene.__next__())

for item in gene:
    print(item)