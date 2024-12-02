class Rectangle:
    def __init__(self,x0,y0,width,height):
        self.x0=x0
        self.y0 = y0
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width*self.height
    def __or__(self,other):
        if self.x0 < other.x0:
            minx = self.x0
        else:
            minx = other.x0
        if self.y0 < other.y0:
            miny = self.y0
        else:
            miny = other.y0
        if self.y0+self.height < other.y0+other.height:
            maxy =  other.y0+other.height
        else:
            maxy = self.y0+self.height
        if self.x0+self.width < other.x0+other.width:
            maxx =  other.x0+other.width
        else:
            maxx = self.x0+self.width
        return "Rectangle: ("+str(minx)+","+str(miny)+")-("+str(maxx)+","+str(maxy)+")"
    def __and__(self,other):
        if self.x0 > other.x0:
            minx = self.x0
        else:
            minx = other.x0
        if self.y0 > other.y0:
            miny = self.y0
        else:
            miny = other.y0
        if self.y0+self.height > other.y0+other.height:
            maxy =  other.y0+other.height
        else:
            maxy = self.y0+self.height
        if self.x0+self.width > other.x0+other.width:
            maxx =  other.x0+other.width
        else:
            maxx = self.x0+self.width
        return "Rectangle: ("+str(minx)+","+str(miny)+")-("+str(maxx)+","+str(maxy)+")"
    def __str__(self):
        return "Rectangle: ("+str(self.x0)+","+str(self.y0)+")-("+str(self.width+self.x0)+","+str(self.height+self.y0)+")"
    def __repr__(self):
        return "rect1"

# rect1 = Rectangle(0,0,10,10)
# rect2 = Rectangle(10,10,10,10)
# #2
# print(rect1.area)
# #3
# rect3 = rect1 | rect2
# print(rect3)
# #4
# rect4 = rect1 & rect2
# print(rect4)
# #5
# print(rect1)
# #6
# print(str(rect1))
# print(rect1==eval(repr(rect1)))

# 連同下面程式上載至e-tutor
cmd ='' 
while True:
    try:
        s = input()
        cmd += s+'\n'
    except EOFError:
        break
p = compile(cmd,'default','exec')
exec(p)