"""
In C/C++,Java,etc.
we have for(i=0;i<10;i++)

In Python , the syntax is changed.

syntax: for i in range(10)

->Print 0 to 9
->Default value starts from 0
->range is inbuilt function
syntax:
        range(start,end,increment)
        
->By default increment is 1.

==============================
4 Variants in For Loop

1)

for i in range(10):
    print(i)
print("**********************************")

2)

for i in range(3,10):
    print(i)

3)

for i in range(1,10,3):
    print(i)
    

4) Reverse

for i in range(10,0,-1):
    print(i)

==========================================    
Programs :
==========================================
1) Sum of N Numbers

n = int(input("Enter N : "))
sum=0
for i in range(1,n+1):
    sum = sum + i

print("Sum : ",sum)


2) Sum of Even and Odd Numbers
==========================================
n = int(input("Enter N : "))
evensum=0
oddsum=0
for i in range(1,n+1):
    if(i%2==0):
        evensum = evensum+i
        
    else:
        oddsum = oddsum + i
        

print("Sum of Even Nos : ",evensum)
print("Sum of Odd Nos : ",oddsum)

3) break keyword
==========================================

for i in range(1,10):
    if(i==5):
        break
    print(i)

4) continue keyword
==========================================

for i in range(1,10):
    if(i==6):
        continue
    else:
        print(i)

5) pass keyword : will be seen in Django more.
                  The pass statement is used as a placeholder for future code.
==========================================

for i in range(1,10):
    if(i==5):
        pass
    else:
        print(i)
"""    





















