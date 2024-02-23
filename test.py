
from geopy.geocoders import Nominatim

adresse="Orgemont sannois"

geolocator = Nominatim(user_agent="app hackathon") #instance
results = geolocator.geocode(adresse, exactly_one=False,addressdetails=True)# Pour obtenir plusieurs résultats si disponibles
list_adresse=[]
for result in results:
    
    list_adresse.append(result)

print(list_adresse)