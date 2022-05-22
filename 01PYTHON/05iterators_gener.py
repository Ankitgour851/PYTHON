'''
Iterable  -
Iterator  -
Iteration -

'''
def gen(n):
    for i in range(n):
        yield i

# print(gen(100000))
# for i in gen(100000):
#     print(i)

ob1 = gen(10)
# print(next(ob1)) 
# print(next(ob1)) 
# print(next(ob1)) 
# print(next(ob1)) 
# print(next(ob1)) 

# print(ob1.__next__())
# print(ob1.__next__())
# print(ob1.__next__())
# print(ob1.__next__())

# for i in ob1:
#     print(i)

num = "harry"
# int cannot be Iterable
# for i in num:
#     print(i)

iter1=iter(num)
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))

# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())

# for i in iter1:
#     print(i)