string = input("Enter String : ")
word = input("Enter word : ")
a=[]
count=0
a = string.split(" ")
for i in range(0,len(a)):
    if word==a[i]:
        count=count+1
print("Count of word is ", count)
