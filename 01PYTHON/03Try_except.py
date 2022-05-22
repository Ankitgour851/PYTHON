# try:
#     open("this.txt")
# except Exception as e:
#     # print(e)
#     pass

# print("Program zinda hai")
# open("this.txt")  





# try:
#     file=open("this.txt","r")
# except EOFError as e:
#     print("eof Error")
# except IOError as e:
#     print("we  can handle this error")

# finally:
#     print("this will print always")



try:
    print("i will try this code and will through exception if there is any problem")
    # open("this.txt")  
except Exception as e:
    print("I will run only if try block will fail")
else:
    print("I will run only if there is no exception. use this to run code which should only execute if there is no exception")
finally:
    print("This will print in every case")