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
