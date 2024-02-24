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
import asyncio
from aiohttp import ClientSession


"""def verifier_adresse(adresse):
    geolocator = Nominatim(user_agent="app hackathon") #instance
    location = geolocator.geocode(adresse)

    ##return location
    if location:
        return "Adresse valide !\nVeuillez vous rendre à cette adresse : " + str(location)
    else:
        return "Adresse invalide. Veuillez vérifier et réessayer."
    """
        
"""def adresse_similaire(adresse):
    geolocator = Nominatim(user_agent="app hackathon") #instance
    results = geolocator.geocode(adresse, exactly_one=False,addressdetails=True)# Pour obtenir plusieurs résultats si disponibles

    if results:
        list_adresse=[]
        for result in results:
          list_adresse.append(result)
        return True, (list_adresse)
    else:
        return False, ""
        """
    
async def recup_adresse(address):#Fonction asynchroniser pour faire des requêtes en arriere plans
    async with ClientSession() as session:
        async with session.get(f"https://nominatim.openstreetmap.org/search?q={address}&format=json") as resultatJSON:
            data = await resultatJSON.json()#Attendre le traitement du fichier JSON
            if data:
                localisation=[]
                adresse=[]
                
                for i in data:   
                    adresse = i.get('display_name')
                    localisation.append(adresse)

                return localisation
            else:
                return None
            #return data
            
async def recup_coordonnees (address):#Fonction asynchroniser pour faire des requêtes en arriere plans
    async with ClientSession() as session:
        async with session.get(f"https://nominatim.openstreetmap.org/search?q={address}&format=json") as resultatJSON:
            data = await resultatJSON.json()#Attendre le traitement du fichier JSON
            if data:
                localisation=[]
                recup_lon=[]
                recup_lat=[]
                recup_lon_lat=[]
                
                for i in data:   
                    recup_lon_lat = i.get('lon'), i.get('lat')
                    localisation.append(recup_lon_lat)

                return localisation
            else:
                return None

async def get_adresse(adresse):#Coroutine principale de asyncio
    Result_adresse = await recup_adresse(adresse)
    return Result_adresse

async def get_coordonnees(adresse):#Coroutine principale de asyncio
    localisation_lon_lat = await recup_coordonnees(adresse)
    return localisation_lon_lat