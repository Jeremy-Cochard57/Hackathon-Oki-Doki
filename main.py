import os
import asyncio

from fonction import get_adresse, get_coordonnees, distance   

adresse_samu="46 Rue Albert Sarraut, 78000 Versailles"
localisation_coordonnees=asyncio.run(get_coordonnees(adresse_samu))


stop = True
while stop:
    #os.system('cls')
    """numéro = input("Veuillez entrer le numéro de la rue : ")
    rue = input("Veuillez entrer la rue : ")
    ville = input("Veuillez entrer la ville : ")
    adresse = numéro + " " + rue + " " + ville
    """
    """adresse=input("Veuillez entrer votre localisation : ")
    valide, message = adresse_similaire(adresse)
    if valide:
        for m in message:
            print(m)
    else:
        print("Aucune adresse trouvée")
    

    if adresse == "stop":
        stop = False"""
    
    adresse_intervention=input("Veuillez entrer votre localisation : ")
    localisation_adresse=asyncio.run(get_adresse(adresse_intervention)) #cas 1 : 12, rue du Faubourg Saint-Antoine, 75011 Paris #cas 2 : 55 Rue des Peupliers

    #list_coo=[]
    #list_coo=asyncio.run(get_coordonnees(adresse_intervention))

    #localisation_coordonnees_input=asyncio.run(get_coordonnees(localisation_adresse))
    #_distance=distance(localisation_coordonnees[0][0], localisation_coordonnees[0][1], list_coo[0][0], list_coo[0][1])


    if localisation_adresse:
        #print("Votre emplacement est : " + str(localisation_adresse)+"\nCoordonnées")
        for i in localisation_adresse:
            print(str(i))
    #print(_distance)
#print(list_coo)