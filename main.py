#Bibliothèque python
import asyncio
import os

#Lien vers le fichier fonction.py
from fonction import TraitementAdresse

stop = True
while stop:
    traitement_adresse=TraitementAdresse()
    adresse_intervention=input("Veuillez entrer votre localisation : ")
    liste_adresses_correspondantes=asyncio.run(traitement_adresse.get_adresse(adresse_intervention)) 
    #Cas 1 : 12, rue du Faubourg Saint-Antoine, 75011 Paris 
    #Cas 2 : 55 Rue des Peupliers
    os.system("cls")

    if liste_adresses_correspondantes:
        print("##############################\nLocalisation disponible : \n")
        for adresses_correspondantes in liste_adresses_correspondantes:
            print(str(adresses_correspondantes))
    print("\nLe position la plus proche du point de repère est : " + str(traitement_adresse.coordonnes_plus_proche()))