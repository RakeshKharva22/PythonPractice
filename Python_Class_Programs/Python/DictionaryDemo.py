d = {1:"Ramesh",2:"Suresh",3:"Kamlesh",4:"Jayesh",5:"Haresh",6:"Sayesh"}
print(d)
print(d[3])
d1 = d.copy()
print(d1)
print(d.get(3))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(5))
print(d)
d.popitem()
print(d)

d2 = {5:"Haresh",6:"Sayesh"}
d.update(d2)
print(d)
d[1] = "Rakesh"
print(d)
d[7] = "Mangesh"
print(d)

for i in d:
    print(i," : ",d[i])
