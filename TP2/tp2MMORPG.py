class Personnage:
    
    def __init__(self, pseudo, niveau:int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__PV = niveau  
        self.__initiative = niveau

    def attaque (self, autre):
        if self.__initiative > autre.__initiative : 
            autre.__PV -= self.__niveau
            if autre.__PV > 0 :
                self.__PV -= autre.__niveau


        elif autre.__initiative > self.__initiative : 
            self.__PV -= autre.__niveau
            if self.__PV >0:
                autre.__PV -= self.__niveau

        else :
            autre.__PV -= self.__niveau
            self.__PV -= autre.__niveau

    def combat (self, autre):
        while self.__PV > 0 and autre.__PV > 0 : 
            self.attaque(autre)

    def soin (self, autre):
        self.__PV = self.__niveau




if __name__ == "__main__":
    
    arthur = Personnage("Arthur", 30)
    lancelot = Personnage("Lancelot", 30)
    
    print("Combat")
    
    arthur.combat(lancelot)