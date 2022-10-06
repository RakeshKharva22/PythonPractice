class A:
    a=0

    def getA(self):
        self.a = int(input("Enter A :"))
        
    def showA(self):
        print("A : ",self.a)

class B(A):
    b=0

    def getB(self):
        self.b=int(input("Enter B :"))

    def showB(self):
        print("B : ",self.b)



n = B()
n.getA()
n.getB()
n.showA()
n.showB()
