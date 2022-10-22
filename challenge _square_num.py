


class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        print("numbers", self.x,self.y,self.z) 
        print("square of numbers",self.x**2,self.y**2,self.z**2)
        print("square sum of numbers",self.x**2+self.y**2+self.z**2)
        
    
         
Point_obj=Point(1,3,5)
Point_obj.sqSum()








        
          