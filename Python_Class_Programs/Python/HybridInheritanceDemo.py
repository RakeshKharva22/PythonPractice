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

class D(B,C):
    d=0

    def getD(self):
        self.d=int(input("Enter D : "))

    def showD(self):
        print("D : ",self.d)
    
d1 = D()

d1.getA()
d1.getB()
d1.getC()
d1.getD()

print("*"*40)

d1.showA()
d1.showB()
d1.showC()
d1.showD()









