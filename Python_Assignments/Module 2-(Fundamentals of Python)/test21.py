name=input("enter a name:")

if(len(name)%4==0):
    print(name[::-1])
else:
    print("String Length is not Multiple of 4.")
