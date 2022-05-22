# ls=[]
# for i in range(100):
#     if i%3==0:
#         ls.append(i)


# ls =[i for i in range(100) if i%3==0]
# print(ls)



# dict1={i:f"item {i}"for i in range(1,1001) if i%100==0}
# dict1={i:f"item {i}"for i in range(5) }
# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n" ,dict2)



# dresses={dress for dress in ["dress1","dress2","dress1","dress2","dress1","dress2"]}
# print(dresses)
# print(type(dresses))



# evens=(i for i in range(100) if i%2==0)
# print(type(evens))
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())

# for item in evens :
#     print(item)

t1=(10,20,"yuvi")
# print(type(t1))

# for i in t1: 
#     print(i)

(i for i in t1)
print(type(t1))
t1=(i for i in t1)
print(type(t1))
t1=tuple(i for i in t1)
# print(t1)
print(type(t1))

t1=(1,2,3,4,5,3)


# for i in t1:
#     print(i*i)

# t1=tuple(i *i for i in t1)
# print(t1)
# print(type(t1))

# (i *i for i in t1)
# print(t1)
# print(type(t1))


