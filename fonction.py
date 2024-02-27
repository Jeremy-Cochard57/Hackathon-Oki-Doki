#Bibliothèque python
import asyncio
import math
from decimal import Decimal

#Bibliothèque importer
from aiohttp import ClientSession

class TraitementAdresse:
    def __init__(self):
        self._adresse_samu = "46 Rue Albert Sarraut, 78000 Versailles"
        self.localisation_adresse_input = None
        self._list_adresse_complete = []
        self._list_longitude_latitude= []
        self._longitude_latitude= []
        self.coordonnes_samu=asyncio.run(self.get_coordonnees(self._adresse_samu))
        self._coordonnees_proche=None

    async def recup_adresse_complete(self, adresse_input):#Fonction asynchroniser pour faire des requêtes en arriere plans
        async with ClientSession() as session:
            async with session.get(f"https://nominatim.openstreetmap.org/search?q={adresse_input}&format=json") as donnes_json:
                resultat_traitement = await donnes_json.json()#Attendre le traitement du fichier JSON
                if resultat_traitement:
                    
                    for clee_json in resultat_traitement:   
                        adresse_complete = clee_json.get('display_name')
                        self._list_adresse_complete.append(adresse_complete)
                    return self._list_adresse_complete
                else:
                    return None
            
    async def recup_coordonnees_long_lat(self, adresse_input):#Fonction asynchroniser pour faire des requêtes en arriere plans
        async with ClientSession() as session:
            async with session.get(f"https://nominatim.openstreetmap.org/search?q={adresse_input}&format=json") as donnes_json:
                resultat_traitement = await donnes_json.json()#Convertion du fichier JSON en object python
                if resultat_traitement:
                    
                    for clee_json in resultat_traitement:   
                        _longitude_latitude = clee_json.get('lon'), clee_json.get('lat')
                        self._list_longitude_latitude.append(_longitude_latitude)

                    return self._list_longitude_latitude
                else:
                    return None

    async def get_adresse(self, adresse_input):#Coroutine principale de asyncio
        self.localisation_adresse_input = adresse_input
        self._list_adresse_complete = await self.recup_adresse_complete(adresse_input)
        return self._list_adresse_complete

    async def get_coordonnees(self, adresse_input):#Coroutine principale de asyncio
        self._list_longitude_latitude = await self.recup_coordonnees_long_lat(self.localisation_adresse_input)
        return self._list_longitude_latitude

    def coordonnes_plus_proche(self):
        distance_min = float('inf')
    

        for element in self._list_longitude_latitude:
            distance_actuelle = math.sqrt((Decimal(self.coordonnes_samu[0][0]) - Decimal(element[0]))**2 + (Decimal(self.coordonnes_samu[0][1]) - Decimal(element[1]))**2)
            if distance_actuelle < distance_min:
                distance_min = distance_actuelle
                self._coordonnees_proche = element
            return element
    







