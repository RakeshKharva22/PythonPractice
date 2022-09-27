a=[]
n = int(input("Enter No. of Elements in List:"))

for i in range(0,n):
    element = input("Enter element"+ str(i+1)+ ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
        max1 = len(i)
        temp = i
print("The word with the longest length is : ",temp," And Length is : ",len(temp))
                    
                    
