import random

data =open("data.txt","w")
for i in range(10):
    num = random.randint(1,999)
    data.write(str(num)+" ");
data.close()
print("*"*58)
data = open("data.txt","r")
#print(data.read())
s = data.read().split(" ")[:-1];
#print(type(s))

for i in s:
    print(int(i))
data.close()

print("*"*80)
data = open("data.txt","r")
even = open("even.txt","w")
odd = open("odd.txt","w")

s = data.read().split(" ")[:-1]
for i in s:
    if int(i)%2==0:
        even.write(i+" ")
    else:
        odd.write(i+" ")
even.close()
odd.close()
data.close()

print("Reading Data File Content")
print()
data = open("data.txt","r")
print(data.read())
data.close()
print("*"*80)
print("Reading Even File Content")
print()
even = open("even.txt","r")
print(even.read())
even.close()
print("*"*80)
print("Reading Odd File Content")
print()
odd = open("odd.txt","r")
print(odd.read())
odd.close()
print("*"*80)












