class A:
    a=0

    def getA(self):
        self.a=int(input("Enter A : "))
        
    def showA(self):
        print("A : ",self.a)

class B:
    b=0

    def getB(self):
        self.b=int(input("Enter B : "))

    def showB(self):
        print("B : ",self.b)

class C(A,B):
    c=0

    def getC(self):
        self.c=int(input("Enter C : "))

    def showC(self):
        print("C : ",self.c)

c = C()
c.getA()
c.getB()
c.getC()

c.showA()
c.showB()
c.showC()






