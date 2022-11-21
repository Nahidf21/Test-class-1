class Point:
    def __init__(self,initx,inity):
        
        self.x=initx
        self.y=inity
        
    def distanceFromOrigin(self):
        
        return ((self.x**2)+(self.y**2))**0.5
    
    def move(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy


""" Test / assert instance parameters """
p=Point(3,4)
assert p.x==3
assert p.y==4


"""test / assert distanceFromOrigin methode"""

assert p.distanceFromOrigin()==5

"""test / assert move methode"""
p.move(2,3)
assert p.x==5
assert p.y==7
