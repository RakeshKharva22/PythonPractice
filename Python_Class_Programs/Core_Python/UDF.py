def MaxofTwo(a,b):
    print("A = ",a,", B = ",b)
    if a>b:
        print(a," Is Greater")
    else:
        print(b," Is Greater")

def MaxofThree(a,b,c):
    print("A = ",a,", B = ",b,", C = ",c)
    if a>b:
        if a>c:
            print(a," Is Greater")
        else:
            print(c," Is Greater")
    elif b>c:
        print(b," Is Greater")
    else:
        print(c," Is Greater")

def EvenOdd(a):
    if a%2==0:
        print(a," Is Even No.")
    else:
        print(a," Is Odd No. ")



def Prime(a):
    if a%2==0:
        print(a," Is not a Prime")
    else:
        for i in range(3,int(a/2)+1,2):
            if a%i==0:
                print(a," Is not a Prime")
                break
            else:
                print(a," Is a Prime")
                break

def Fibonacci(n):
    a,b=0,1
    while b<n:
        print(b,end=" ")
        a,b = b,a+b

        
    



