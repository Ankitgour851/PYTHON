f1=open("1.txt")

try:
    f=open("doesnt1.txt")
# except Exception as e:
#     print(e)

except EOFError as e:
    print("Print eof error a gaya hai",e)

except IOError as e:
    print("Print eof error a gaya hai",e)

else:
    print("this will run only if except will not run")


finally:
    print("Run this anyway......")
    # f.close()
    f1.close()

print("important file")
