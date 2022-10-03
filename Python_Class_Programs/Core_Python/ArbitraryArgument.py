"""
#1.

def test(a,b,c,*d):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

#The last argument will print in tuple format.
test(1,2,3,4)


#2. ArbitraryArgument     
def test(a,b,c,*d):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",d)

test(1,2,3,4,5,6,7,8)

# 3. Convert into List Format
def test(a,b,c,*d):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",list(d))

test(1,2,3,4,5,6,7,4)
"""
#4. Converting into Data Dictionary
def test(a,b,c,*d,**e):
    print("A : ",a,",B : ",b,",C : ",c,",D : ",list(d),",E : ",e)

test(1,2,3,4,5,6,7,8,9,12,x=87,y=41,z=43)

