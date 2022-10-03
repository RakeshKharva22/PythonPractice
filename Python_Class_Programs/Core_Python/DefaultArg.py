"""
def test(a,b,c,d):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test(10,20,30,40)

def test(a,b,c,d=20):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test(1,2,3)



def test(a,b,c = 30,d=20):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test(1,2)

"""

def test(a=40,b=20,c=30,d=10):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test()

#Keyword Argument

def test(a=40,b=30,c=20,d=10):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test(b=1,d=3)








