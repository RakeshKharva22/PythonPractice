class A:
    def show(self):        
        print("Show from A")
    
class B(A):
    def show(self):
        super().show()
        print("Show from B")

class C(B):
    def show(self):
        super().show()
        print("Show from C")


c = C()
c.show()
