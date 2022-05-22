class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash +=ord(char)
        return hash%self.MAX

    def __getitem__(self,key):
        h = self.get_hash(key)
        for kv in self.arr[h]:
            if kv[0] == key:
                return kv[1]
        
    def __setitem__(self,key,val):
        h =self.get_hash(key)

        found = False
        for idx,element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True

        if not found:
            self.arr[h].append((key,val))

    def __delitem__(self,key):
        arr_index=self.get_hash(key)
        for index,kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print(f"deleting element at {index}")
                del self.arr[arr_index][index]

t = HashTable()
print(t.get_hash('march 6'))
print(t.get_hash('march 17'))

t["march 6"] = 120
t["march 6"] = 45
t["march 8"] = 67
t["march 9"] = 4
t["march 17"] = 459

print(t["march 6"])
print(t["march 17"])
t["march 30"] = 78888
print(t["march 17"])


print(t.arr)
del t["march 30"]
print(t.arr)

