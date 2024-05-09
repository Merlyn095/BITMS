class circle:
    def __init__(self,radius):
        self.r=radius
    def printing(self):
        a=3.142*self.r*self.r
        print(a)
class rectangle:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth
    def printing(self):
        area=self.l*self.b
        print(area)   
l=float(input("rectangle"))
b=float(input("rectangle"))
r=float(input())
o=circle(r)
o1=rectangle(l,b) 
o.printing()
o1.printing()   