class MyClass:
    x=0

    def __init__(self,x):
        self.x=x
        #print(self.x,"Init Called")

    def mymethod(self):
        print("X : ",self.x)

    def OddEven(self):
        if self.x%2==0:
            print(self.x," Is Even No.")
        else:
            print(self.x," Is Odd No.")
    
x = int(input("Enter No. "))

a = MyClass(x)
a.mymethod()
a.OddEven()
