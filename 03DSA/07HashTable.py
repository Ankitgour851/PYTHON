stock_prices = [['march 6',310.0],['march 7',340.0],['march 8',380.0],['march 9',302.0],['march 10',297.0],['march 11',323.0]]
for element in stock_prices:
    if element[0] == 'march 11':
        print(element[1])
print(ord('a'))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None]*self.MAX

    def get_hash(self,key):
        sum = 0
        for c in key:
            sum +=ord(c)
        return sum%self.MAX

    def __setitem__(self,key,val):
        h =self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return self.arr[h]

    def __delitem__(self,key):
        h =self.get_hash(key)
        self.arr[h] = None

h=HashTable()
# print(h.arr)
h['march 6'] = 302
h['march 11'] = 78
# print(h.arr)
print(h['march 6'])
print(h['march 11'])
del h['march 11']
print(h['march 11'])



