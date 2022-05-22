# *args and **kwargs
# *vars and **kvars

# def function_1(name,age,rollno):
#     print("The name of the student is",name," and age is ",age," and  rollno is ", rollno)


def function_1(*args):
    # print(type(args))
    if(len(args)==3):
        print("The name of the student is",args[0]," and age is ",args[1]," and  rollno is ",args[2])
    else:
        print("The name of the student is",args[0]," and age is ",args[1])

def printmarks(**kwargs):
    # print(type(kwargs))
    for key,value in kwargs.items():
        print(key,value)

def master(normal,*args,**kwargs):
    print(normal)
    for i in args:
        print(i)
    for key,value in kwargs.items():
        print(key,value)


lis=["harry",22,345]
# function_1(*lis)
# function_1("harry", 22,345)
# function_1("harry",22)


marklist={"harry":100,"Rohandas":97,"Aman":91,"theprogrammer":80,"Maaniverma":89,"Sanket":86,"gaming with honey":77}
# printmarks(**marklist)


master("normal arg",*lis,**marklist)