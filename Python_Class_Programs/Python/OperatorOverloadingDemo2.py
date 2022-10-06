class Point:

    def __init__(self,x,y):
        print("Init Called")
        self.x = x
        self.y = y

    def __str__(self):
        print("str called")
        return "[{0},{1}]".format(self.x,self.y)

    def __add__(self,obj):
        print("add called")
        x = self.x+obj.x
        y = self.y+obj.y
        return Point(x,y)

p1 = Point(10,20)
print(p1)
p2 = Point(4,5)
print(p2)
print("*"*40)
print("Addition : ",(p1+p2))
print("*"*40)
