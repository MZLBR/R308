import math

class point:
    def __init__(self, x: float = 0, y: float = 0):
        self.__x = x
        self.__y = y
    def __str__(self) -> str:
        return f"point:[{self.__x};{self.__y}]"
    def get_x(self) -> float: return self.__x
    def get_y(self) -> float: return self.__y
    def distanceCoordonnee(self, x: float, y: float) -> float: 
        return math.sqrt((self.__x - x)**2 + (self.__y - y)**2)

class Cercle:
    # Gère les 2 modes : Cercle(5) OU Cercle(3, point(1,2))
    def __init__(self, rayon: float, centre: point = point(0, 0)):
        self.__rayon = rayon
        self.__centre = centre

    def calculerDiametre(self) -> float:
        return 2 * self.__rayon

    def calculerPerimetre(self) -> float:
        return 2 * math.pi * self.__rayon

    def calculerSurface(self) -> float:
        return math.pi * (self.__rayon ** 2)

    def estEnIntersection(self, autre: "Cercle") -> bool:
        d = self.__centre.distanceCoordonnee(autre.__centre.get_x(), autre.__centre.get_y())
        return d <= (self.__rayon + autre.__rayon)

    def contientPoint(self, A: point) -> bool:
        d = self.__centre.distanceCoordonnee(A.get_x(), A.get_y())
        return d <= self.__rayon

if __name__ == "__main__":
    # Test Mode 1 (Origine) et Mode 2 (Centre défini)
    c1 = Cercle(5.0)
    c2 = Cercle(3.0, point(3, 4))
    
    # Tests des 5 méthodes
    print("1. Diamètre:", c1.calculerDiametre())
    print("2. Périmètre:", c1.calculerPerimetre())
    print("3. Surface:", c1.calculerSurface())
    print("4. Intersection:", c1.estEnIntersection(c2))
    print("5. Contient point (1,1):", c1.contientPoint(point(1, 1)))

