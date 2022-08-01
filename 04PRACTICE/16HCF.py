a = int(input("Enter first number \n"))
b = int(input("Enter second number \n"))

# maxNum = max(a, b)
# print("the",maxNum)

# while(True):
#     if (a%maxNum == 0) and (b%maxNum == 0):
#         break
#     maxNum -=1

# print(f"The HCf of {a} and {b} is {maxNum}")

minNum = min(a, b)
for i in range(1,minNum+1):
    if a%i==0 and b%i==0:
        HCF = i
print(f"The HCF of {a} and {b} is",HCF)
