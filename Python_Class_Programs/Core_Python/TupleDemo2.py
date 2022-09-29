t = (1,2,3,1.1,2.2,"tops",True,[100,200,300],10,True,"python",1,2)
print(t)
print(t[7])
t[7].append(400)
print(t)
print(t[7])

for i in t:
    print(i)

print("top" in t)
