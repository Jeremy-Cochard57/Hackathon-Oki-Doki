from pygeocoder import Geocoder

def verifier_adresse(adresse):
    try:
        resultat = Geocoder.geocode(adresse)
        if resultat.valid_address:
            return True, "Adresse valide."
        else:
            return False, "Adresse invalide. Veuillez vérifier et réessayer."
    except Exception as e:
        return False, str(e)