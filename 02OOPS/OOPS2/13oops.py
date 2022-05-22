class A:
    def met(self):
        print("This is methof from class A")
    
class B(A):
    def met(self):
        print("This is methof from class B")

class C(A):
    def met(self):
        print("This is methof from class C")
    

class D(C,B):
     def met(self):
        print("This is methof from class D")
    
    
a=A()
b=B()
c=C()
d=D()

d.met()