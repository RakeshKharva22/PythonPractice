a = int(input("Enter A : "))
b = int(input("Enter B : "))
print("Before Swap A = ",a,", B = ",b)
"""
temp = a
a = b
b = temp
"""
a,b = b,a
print("After Swap A = ",a,", B = ",b)
