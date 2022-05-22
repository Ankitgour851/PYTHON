import bisect

number = 3
a = [1,2,4,6,7,8,9,34]
# a=[2,121,4,56,3,54]  list is always sorted to use bisect module

print(bisect.bisect(a, number))
bisect.insort(a,number)
print(a)