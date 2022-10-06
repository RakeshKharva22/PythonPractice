class A:
    def show(self):
        super().show()
        print("Show from A")

class B:
    def show(self):
        print("Show from B")

class C(A,B):
    def show(self):
        super().show()
        print("Show from C")

c = C()
c.show()
    
