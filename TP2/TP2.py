class Personnage:
    
    def __init__(self, pseudo : str, niveau:int = 1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__PV = niveau  
        self.__initiative = niveau

    def __str__(self) -> str:
        return f"le personnage {self.__pseudo} est niveau {self.__niveau} avec {self.__PV} point de vie et {self.__initiative} d'initiative"

    @property
    def get_pseudo(self) -> str:
        return self.__pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    @property
    def initiative(self) -> int:
        return self.__initiative

    @property
    def PV(self):
        return self.__PV

    @PV.setter
    def PV(self, point : int):
        self.__PV = point
        

    def attaque (self, attaque: "Personnage"):
        if self.__initiative > attaque.__initiative : 
            attaque.__PV -= self.degats()
            if attaque.__PV > 0 :
                self.__PV -= attaque.degats()


        elif attaque.__initiative > self.__initiative : 
            self.__PV -= attaque.degats()
            if self.__PV >0:
                attaque.__PV -= self.degats()

        else :
            attaque.__PV -= self.degats()
            self.__PV -= attaque.degats()

    def combat (self, opposant : "Personnage"):
        while self.__PV > 0 and opposant.__PV > 0 : 
            self.attaque(opposant)

        if self.__PV > 0 :
            return self
        elif opposant.__PV >0:
            return opposant
        else:
            return None
    

    def soin (self, opposant):
        self.__PV = self.__niveau

    def degats ( self):
        return self.niveau


class Guerrier (Personnage) : 

    def __init__(self, pseudo: str, niveau: int = 1):
        super().__init__(pseudo, niveau)
        self.PV = niveau * 8 + 4
        self.init = niveau * 4 + 6
#Guerrier1 = Guerrier("toto")
#print(vars(Guerrier))

    def degats(self):
        return self.niveau*2

class Mage (Personnage) : 
    def __init__(self, pseudo: str, niveau: int = 1, PV : int =1 , initiative : int = 1):
        super().__init__(pseudo, PV, initiative)
        self.PV= niveau *5+10
        self.initiative= niveau*6+4
        self.__mana = niveau *5 

    @property
    def mana(self)->int:
        return self.__mana

    @mana.setter
    def mana(self,points_mana : int):
        self.__mana = points_mana

    def degats(self):
        if self.mana >=4:
            self.mana -=4
            return self.niveau + 3
        else : 
            return self.niveau
    





if __name__ == "__main__":
    
    htz = Personnage("htz",23)
    mz = Personnage("mz", 3)
    print("Combat")
    gagnant=htz.combat(mz)
    if gagnant ==htz:
        print(f"Le gagnant est {htz.get_pseudo} avec {htz.PV}")
    elif gagnant==mz:
        print(f"Le gagnant est {mz.get_pseudo} avec {mz.PV}")
    else:
        print(f"egalité")