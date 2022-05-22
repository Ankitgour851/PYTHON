class A:
    classvar1="I am in class variable in class A"
    def __init__(self):
        self.var1="I am in class A constructor"
        self.classvar1="Instance var in class A"
        self.special="Special"

class B(A):
    classvar1="I am in class variable in class B"
    def __init__(self):
        super().__init__()
        self.var1="I am in class B constructor"
        self.classvar1="Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a=A()
b=B()
print(b.special,a.var1,a.classvar1)