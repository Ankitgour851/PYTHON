import json

data='{"var1":"harry","var2":56}'
print(data)
# print(data['var1'])

parsed=json.loads(data)
print(parsed)
print(type(parsed))
print(parsed['var1'])

# Task 1 - jason.load?
# ye java script mai jo likha hai use python mai convert krr deta jisse wo padne mai asan ho jata hai
#  Task 2 - what is sort keys parameter in dumps


data2={"Channel_name":"codewithharry",
        "cars":['bmw','audi a8','ferrari'],
        "Fridge":('roti',540),
        "isbad":False}

jscomp=json.dumps(data2)
print(jscomp)