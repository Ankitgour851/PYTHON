
sum = 0
while(True):
    userinput = input("Enter the item price or q to exit: \n")
    if (userinput!='q'):
        sum=sum+int(userinput)
        print(f'order total so far:{sum}')
    
    else:
        print(f"Your total bill is {sum}.thanks for using our calculator")
        break 