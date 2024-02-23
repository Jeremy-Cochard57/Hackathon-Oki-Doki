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
from geopy.adapters import AioHTTPAdapter


def verifier_adresse(adresse):
    geolocator = Nominatim(user_agent="app hackathon") #instance
    location = geolocator.geocode(adresse)

    ##return location
    if location:
        return "Adresse valide !\nVeuillez vous rendre à cette adresse : " + str(location)
    else:
        return "Adresse invalide. Veuillez vérifier et réessayer."
        
def adresse_similaire(adresse):
    geolocator = Nominatim(user_agent="app hackathon") #instance
    results = geolocator.geocode(adresse, exactly_one=False,addressdetails=True)# Pour obtenir plusieurs résultats si disponibles

    if results:
        list_adresse=[]
        for result in results:
          list_adresse.append(result)
        return True, (list_adresse)
    else:
        return False, ""