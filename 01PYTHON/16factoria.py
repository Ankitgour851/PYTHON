def factorial(number):
    factorial=1 
    if (number<0):
        print("Error:Factorial of a negative number is not defined")

    elif(number==0):
        return 1

    else:
        for i in range(1,number+1):
            factorial=factorial*i
        return factorial


if __name__ == '__main__':
    print("Enter the number")
    number=int(input())
    print("the factorial of the ",number,"is ",factorial(number))

    # factorial=1 
    # if (number<0):
    #     print("Error:Factorial of a negative number is not defined")

    # elif(number==0):
    #     print(1)

    # else:
    #     for i in range(1,number+1):
    #         factorial=factorial*i
    #     print("the factorial of the ",number,"is ",factorial)
