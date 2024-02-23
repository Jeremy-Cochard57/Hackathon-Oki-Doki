import os

from fonction import verifier_adresse

stop = True
while stop:
    os.system('cls')
    numéro = input("Veuillez entrer le numéro de la rue : ")
    rue = input("Veuillez entrer la rue (sans les caractères spéciales) : ")
    ville = input("Veuillez entrer la ville (sans les caractères spéciales) : ")
    adresse = numéro + rue + ville
    valide, message = verifier_adresse(adresse)
    print(message)

    if adresse == "stop":
        stop = False