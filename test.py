import math

def coordonnes_plus_proche(coordonnees, coordonnes_samu):
    coordonnees_proche = None
    distance_min = float('inf')
    
    for element in coordonnees:
        distance_actuelle = math.sqrt((coordonnes_samu[0] - element[0])**2 + (coordonnes_samu[1] - element[1])**2)
        if distance_actuelle < distance_min:
            distance_min = distance_actuelle
            coordonnees_proche = element
            
    return coordonnees_proche

coordonnees = [(5.8877979, 48.6684041), (5.5187049, 45.4289016), (2.32529, 48.780794), (48.780794, 48.8216589), (-71.3043579, 46.6568968)]
coordonnes_samu = (2.1500621, 48.7941196)
plus_proche = coordonnes_plus_proche(coordonnees, coordonnes_samu)
print("Les coordonnées les plus proches de", coordonnes_samu, "sont", plus_proche)