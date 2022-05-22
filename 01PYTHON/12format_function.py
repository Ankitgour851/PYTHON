'''
printf(%d or %s)  in python

format function
'''

user=['rohan das','shubham','skill f','mahimudul hussain']
computer=['rasberry pi','android','iphone','100rs walla comp']

# for i in range(0,len(user)):
#     print("computer used by",user[i],'is',computer[i])

for i in range(0,len(user)):
    # template="computer used by {} is {}"
    template="computer used by {1} is {0}"
    print(template.format(user[i],computer[i]))
