import os

from fonction import verifier_adresse

stop = True
while stop:
    #os.system('cls')
    numéro = input("Veuillez entrer le numéro de la rue : ")
    rue = input("Veuillez entrer la rue : ")
    ville = input("Veuillez entrer la ville : ")
    adresse = numéro + " " + rue + " " + ville
    valide, message = verifier_adresse(adresse)
    print(message)
    print(adresse)
    

    if adresse == "stop":
        stop = False