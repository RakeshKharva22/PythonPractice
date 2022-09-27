n = int(input("Enter N :"))
sum=0
if n>0:
    for i in range(1,n+1):
        sum=sum+i

    print("Sum of N Positive is :",sum)
else:
    print("Please Enter +ve No.")
