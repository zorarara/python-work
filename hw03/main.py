import math
class shapes():
    def __init__(self,a,b):
        self.a=a
        self.b=b
class ellipse(shapes):
pi=3.1415926535
    def area(self):
        return( self.a*self.b*math.pi)
class circle(ellipse):
    pass
    
class rectangle(shapes):
    def area(self,width,height):
        return(self.width*self.height)
class square(rectangle):
    pass

def compute_area(shapes):
    return sum(i.area() for i in shapes)

shapes=[ellipse(10,20),square(15,15),circle(5,5),rectangle(20,15),circle(5,5)
        ,square(15,15),ellipse(10,20)]
total_area=sum(area)
print('图形的面积之和=',total_area) 
