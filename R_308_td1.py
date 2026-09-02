def plus_grand_nombre (a : float, b : float) -> int :
    """
    fonction qui retourne le plus grand de deux nombres réels
    a : nbr choisi 
    b : nbr choisi
    """
    if a > b :
        return a 
    else : 
        return b 
    
print(plus_grand_nombre(4,5))

#--------------------------------------------------------------------

def seuil (a : int, b=10 ) -> int :
    """
    indique si la valeur passée est supérieure à 10 
    a : nbr choisi
    b : seuil = 10
    """
    if a > b : 
        return (f"{a} est supérieur au seuil")
print(seuil(11,20))

#---------------------------------------------------------------------

def list (a : list ) -> int : 
    """
    retourne le max de la liste
    """
    return max (*a)

print(list([3,7,2,9,5,13,2]))

#--------------------------------------------------------------------------

def listseuil (a : list, b=3) -> int : 

    compteur = 0
    for v in a :
        if v < b :
            compteur += 1

    return compteur
print (listseuil([2,4,18,4,2,1,23,0]))


#----------------------------------------------------------------------------

def ensemble (a: list ) ->int :

    