a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))

maxNum = max(a, b)
print("the",maxNum)

while(True):
    if (maxNum%a == 0) and (maxNum%b == 0):
        break
    maxNum +=1

print(f"The LCM of {a} and {b} is {maxNum}")
