"""import geocoder

def verifier_adresse(adresse):
    try:
        resultat = geocoder.geocode(adresse)
        if resultat.valid_address:
            return True, "Adresse valide."
        else:
            return False, "Adresse invalide. Veuillez vérifier et réessayer."
    except Exception as e:
        return False, str(e)
        """

from geopy.geocoders import Nominatim

def verifier_adresse(adresse):
    geolocator = Nominatim(user_agent="app hackathon") #instance
    location = geolocator.geocode(adresse)

    ##return location
    if location:
        return True, "Adresse valide !\nVeuillez vous rendre à cette adresse : " + str(location)
    else:
        return False, "Adresse invalide. Veuillez vérifier et réessayer."
        