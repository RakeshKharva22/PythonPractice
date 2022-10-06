import UDF

while True:
    print("*"*50)
    print("Press 1.MaxofTwo")
    print("Press 2.MaxofThree")
    print("Press 3.EvenOdd")
    print("Press 4.Prime No")
    print("Press 5.Fibonacci")
    print("Press 6.Exit")
    print("*"*50)

    print()
    choice = int(input("Enter your choice ?"))

    if choice==1:
        n1=int(input("Enter A : " ))
        n2=int(input("Enter B : " ))
        UDF.MaxofTwo(n1,n2)
    elif choice==2:
        n1=int(input("Enter A : " ))
        n2=int(input("Enter B : " ))
        n3=int(input("Enter C : " ))
        UDF.MaxofThree(n1,n2,n3)
    elif choice==3:
        n3=int(input("Enter No. : " ))
        UDF.EvenOdd(n3)
    elif choice==4:
        n=int(input("Enter No : " ))
        UDF.Prime(n)
    elif choice==5:
        n3=int(input("Enter No : " ))
        UDF.Fibonacci(n3)
        print()
    else:
        break
   
    


