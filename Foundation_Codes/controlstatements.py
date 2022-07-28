"""""
Control Statements

1) Simple If
    if condition:

e.g

    

2) if/else

    if condition:
        statement
    else
        statement

3) Nested if/else

    if condition:
        if condition:
            statement
        else:
            statement
    else:
        if condition:
            statement
        else:
            statement

4) Ladder if/else

    if condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    elif condition:
        statement
    else:



"""

"""""
print("------Simple If ---------")
num1 = int(input("Enter No : "))

if num1>0:
    print(num1, " is +ve")

print("-------IF/ELSE------------")
num = int(input("Enter a Number : "))

if num%2==0:
    print(num, " is Even")
else:
    print(num, " is Odd")

"""

"""""
print("---------Nested If/else----------")

num1 = int(input("Enter No.1 : "))
num2 = int(input("Enter No.2 : "))
num3 = int(input("Enter No.3 : "))
print()
print("Num1 = ",num1," Num2 = ",num2," Num3 = ",num3)
print()
if num1>num2:    
    if num1>num3:
        print(num1," is Greater")
    else:
        print(num3, "is Greater")
else:
    if num2>num3:
        print(num2," is Greater")
    else:
        print(num3, " is Greater")

print()

"""
print("---------Ladder If/else----------")
print()
print("---------Enter Details------------")
print()
id= int(input(" Enter Roll.No : "))
name = input("Enter Name : ")
phy= int(input("Enter Physics Marks : "))
chem = int(input("Enter Chemistry Marks : "))
maths = int(input("Enter Maths Marks : "))
total = phy+chem+maths
per = total/3
print()
print("---------Display Details------------")
print()
print("Roll No. is : ",id)
print("Name is : ", name)
print("Total Marks : ",total)
print("Percentage is : ",per)

if per>75:
    print("Distinction")
elif per>60:
    print("Grade A")
elif per>50:
    print("Grade B")
elif per>40:
    print("Grade C")
else:
    print("Fail")


