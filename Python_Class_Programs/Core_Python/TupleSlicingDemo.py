
#    0 1 2  3   4    5          6          7  8     9    0 1  2    3 4 5  + 
t = (1,2,3,1.1,2.2,"pyhton",[100,200,300],10,True,"tops",1,2,False,7,8,4)
#    6 5 4  3   2   1        0            9  8     7     6 5 4     3 2 1  -

print(t[::12])
print(t[14:])
print(t[:3:3])
print(t[1:14:7])
print(t[-14::])
print(t[::-2])
print(t[:-1:-3])
print(t[-14:-12:2])
print(t[-10:-7])
