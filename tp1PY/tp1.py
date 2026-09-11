import math

class point:
    def __init__(self, x:int=0 ,y:int=0 ):
        self.__x=x
        self.__y=y
    def __str__(self) -> str :
        return f"point:[{self.__x};{self.__y}]"
    
    def distanceCoordonnee (self,x : float,y: float) -> float : 
        distance=math.sqrt((self.__x-x)**2+(self.__y-y)**2)
        (math.pow(self.__x-x,2)+math.pow(self.__y-y,2))
        ((self.__x-x)*(self.__x-x)+(self.__y-y)*(self.__y-y))
        return distance 

if __name__ =="__main__":
    p1 = point(3.2,1)
    print(p1)
    p2=point()
    print(p2) 
    point:[0,0]
    print(p1.distanceCoordonnee(0,0))