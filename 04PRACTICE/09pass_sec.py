
SECURE = (('s','$'),('and','&'),('a','@'),('o','0'),('i','1'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("enter your password\n")
    password = securePassword(password)
    print(f"your secur password is {password}")