
"""
1) Simple If

a = int(input("Enter No."))
if(a>0):
    print(a,"is +ve No.")

2) if/else

a = int(input("Enter No."))
if(a>0):
    print(a,"is +ve No.")
else:
    print(a,"is -ve No.")

WAP to find EVEN ODD
WAP to find Greater of 2


3) Nested if/else

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))
print("A = ",a,",B = ",b,",C = ",c)
if(a>b):
    if(a>c):
        print("A is Greater")
    else:
        print("C is Greater")
else:
    if(b>c):
        print("B is Greater")
    else:
        print("C is Greater")
"""
a=int(input("Enter Roll No :"))
name = input("Enter Name :")
s1 = int(input("Enter Physics Marks : "))
s2 = int(input("Enter Chemistry Marks : "))
s3 = int(input("Enter Maths Marks : "))
total = s1+s2+s3
per = total/3
print("Total Marks : ",total)
print("Percentage : ",per)

if(per>=75):
    print("Distinction")
elif(per>=60):
    print("First Class")
elif(per>=50):
    print("Second Class")
elif(per>=40):
    print("Pass Class")
else:
    print("Fail!")



















    


