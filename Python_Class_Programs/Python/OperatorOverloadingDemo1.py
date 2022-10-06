"""
class Point:

    def __init__(self):
        print("Init Method Called")
   
p = Point()


class Point:

    def __init__(self,x,y):
        print("Init Called")
        print("X : ",x,"Y : ",y)

p = Point(10,20)

"""
class Point:

    def __init__(self,x,y):
        print("Init Called")
        self.x = x
        self.y = y

    def __str__(self):
        return "[{0},{1}]".format(self.x,self.y)

p = Point(10,20)
print(p)
