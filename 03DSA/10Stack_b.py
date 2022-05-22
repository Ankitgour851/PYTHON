from collections import deque
stack = deque()
# print(dir(deque()))
stack.append('https://www.cnn.com/')
# print(stack)
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')
print(stack)

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.pop()

print(stack)
