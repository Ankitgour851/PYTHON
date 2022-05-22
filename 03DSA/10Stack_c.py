from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
print(s)

print(s.is_empty())
print(s.pop())
print(s.is_empty())

s.push(5)
s.push(7)
s.push(45)
s.push(12)

print(s.peek())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

print(s.pop())
