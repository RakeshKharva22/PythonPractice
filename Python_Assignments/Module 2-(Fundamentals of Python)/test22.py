string=input("Enter string:")
count=0

if len(string)>=2:
    for i in string:
          count=count+1
    new=string[0:2]+string[count-2:count]
    print("Newly formed string is:")
    print(new)
