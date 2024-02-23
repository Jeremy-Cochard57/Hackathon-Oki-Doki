import os
import asyncio

from fonction import verifier_adresse,adresse_similaire

stop = True
while stop:
    #os.system('cls')
    """numéro = input("Veuillez entrer le numéro de la rue : ")
    rue = input("Veuillez entrer la rue : ")
    ville = input("Veuillez entrer la ville : ")
    adresse = numéro + " " + rue + " " + ville
    """
    adresse=input("Veuillez entrer votre localisation : ")
    valide, message = adresse_similaire(adresse)
    if valide:
        for m in message:
            print(m)
    else:
        print("Aucune adresse trouvée")
    

    if adresse == "stop":
        stop = False