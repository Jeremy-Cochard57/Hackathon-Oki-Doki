import asyncio
from geopy.geocoders import Nominatim
from aiohttp import ClientSession

async def recup_coordonnees(address):#Fonction asynchroniser pour faire des requêtes en arriere plans
    async with ClientSession() as session:
        async with session.get(f"https://nominatim.openstreetmap.org/search?q={address}&format=json") as resultatJSON:
            data = await resultatJSON.json()#Attendre le traitement du fichier JSON
            """if data:
                localisation=[]
                recup_lon=[]
                recup_lat=[]
                recup_lon_lat=[]
                
               for i in data:
                   
                    recup_lon = i.get('lon')
                    recup_lat = i.get('lat')
                    recup_lon_lat=recup_lon+""+recup_lat

                    localisation.append(recup_lon_lat)

                return localisation
            else:
                return None"""
            return data

async def main(adresse):#Coroutine principale de asyncio
    localisation_lon_lat = await recup_coordonnees(adresse)
    return localisation_lon_lat 
            
        

# Exécute la boucle principale asyncio
adresse=input("Veuillez entrer votre localisation : ")
localisation_lon_lat=asyncio.run(main(adresse))
print("Votre emplacement est : " + str(localisation_lon_lat))
