def gen(n):
    for i in range(n):
        yield i

g = gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h="harry"
# h=3382923
ier=iter(h)
print(ier.__next__())
print(ier.__next__())
print(ier.__next__())




# print(h[0])
# for c in h:
#     print(c)

