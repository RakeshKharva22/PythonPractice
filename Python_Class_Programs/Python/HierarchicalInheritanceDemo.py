class A:
    a=0

    def getA(self):
        self.a=int(input("Enter A : "))
        
    def showA(self):
        print("A : ",self.a)

class B(A):
    b=0

    def getB(self):
        self.b=int(input("Enter B : "))

    def showB(self):
        print("B : ",self.b)

class C(A):
    c=0

    def getC(self):
        self.c=int(input("Enter C : "))

    def showC(self):
        print("C : ",self.c)

class D(A):
    d=0

    def getD(self):
        self.d=int(input("Enter D : "))

    def showD(self):
        print("D : ",self.d)
    

b1 = B()
c1 = C()
d1 = D()
print("*"*40)
b1.getA()
b1.getB()
c1.getC()
d1.getD()

print("*"*40)
b1.showA()
b1.showB()
c1.showC()
d1.showD()









