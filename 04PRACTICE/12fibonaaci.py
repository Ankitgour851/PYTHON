import time

def fibiter(n):
    prevnum = 0
    currentno = 1
    for i in range(1,n):
        prevprev = prevnum
        prevnum = currentno
        currentno = prevnum + prevprev
    return currentno

def fibrecur(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibrecur(n-1) + fibrecur(n-2)

num = int(input("Enter the number"))
init = time.time()
print(f"using recursion value of fib{num} is {fibrecur(num)}")
print(f"It took {time.time() - init} seconds")
init = time.time()
print(f"using iteration value of fib{num} is {fibiter(num)}")
print(f"It took {time.time() - init} seconds")
