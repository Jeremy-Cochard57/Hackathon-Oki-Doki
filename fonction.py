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
import math

#def __init__():
    

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
                _localisation_adresse=[]
                adresse=[]
                
                for i in data:   
                    adresse = i.get('display_name')
                    _localisation_adresse.append(adresse)

                return _localisation_adresse
            else:
                return None
            #return data
            
async def recup_coordonnees (address):#Fonction asynchroniser pour faire des requêtes en arriere plans
    async with ClientSession() as session:
        async with session.get(f"https://nominatim.openstreetmap.org/search?q={address}&format=json") as resultatJSON:
            data = await resultatJSON.json()#Attendre le traitement du fichier JSON
            if data:
                _localisation_coordonnes=[]
                recup_lon=[]
                recup_lat=[]
                recup_lon_lat=[]
                
                for i in data:   
                    recup_lon_lat = i.get('lon'), i.get('lat')
                    _localisation_coordonnes.append(recup_lon_lat)

                return _localisation_coordonnes
            else:
                return None

async def get_adresse(adresse):#Coroutine principale de asyncio
    Result_adresse = await recup_adresse(adresse)
    return Result_adresse

async def get_coordonnees(adresse):#Coroutine principale de asyncio
    _localisation_lon_lat = await recup_coordonnees(adresse)
    return _localisation_lon_lat

"""def distance(coord_a_a, coord_a_b, coord_b_a, coord_b_b):
    _distance_lat=math.dist(coord_a_a, coord_b_a)
    _distance_lon=math.dist(coord_a_b, coord_b_b)
    return _distance_lat, _distance_lon
    """

def compare_dist(coordonnes_samu, list_coordonnes):
    result_list_coordonnes=""
    result_list_coordonnes=i
    for i in list_coordonnes:
        
        if i>result_list_coordonnes:
            result_list_coordonnes=i

    return list_coordonnes


