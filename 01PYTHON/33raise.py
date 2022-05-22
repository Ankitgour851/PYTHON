# a=input("What is your name")
# b=input("how much do you earn")
# if int(b)==0:
#     raise ZeroDivisionError("B is o so stopping the program")
# if a.isnumeric():
#     raise Exception("Numbers is not allowed")

# print(f"Hello {a}")


c=input()
try:
    print(a)
except Exception as e:
    if c=="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")