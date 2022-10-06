l = [1,2,3,1.1,'tops',False,True,1,2,10,'Python']
print(l)
l.append(100)
print(l)
l1 = l.copy()
print(l1)
l2 = l1.copy()
print(l2)
l1.append(200)
print(l1)
l2.append(200)
print(l2)
print(l)
l2 = l;
print(l2)
print(l)
l.pop()
print(l2)
print(l)
print(l1)
print(l.count(1))
print(l.count(0))

l3 = [1000,2000,3000]
l.extend(l3)
print(l)
print(l.index(10))
l.insert(5,1001)
print(l)
l.remove(2000)
print(l)

l.reverse()
print(l)

for i in l:
    print(i)
print(10 in l)

    












