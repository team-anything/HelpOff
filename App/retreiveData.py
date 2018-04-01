from googleplaces import GooglePlaces, types, lang
import sys
from config import *


YOUR_API_KEY = "AIzaSyAlKXS0K2tTl3a2wFeDmuzESqrFG-OVKpw"
google_places = GooglePlaces(YOUR_API_KEY)

'''
# TEXT_SEARCH
query_result = google_places.text_search(query="Restaurant in Dahisar",location="Mumbai,India",radius=2000)

# AUTOCOMPLETE
query_result = google_places.autocomplete(input="Dahisar w",location="Mumbai,India",radius=200)
print(query_result.predictions)
'''

# print(dir(types))
# NEARBY AREA SEARCH

def retreive_area(loc,key):
    # temps here
    query_result = google_places.nearby_search(
    location=loc, keyword=key,
        radius=1000,types=[types.TYPE_HOSPITAL])
    '''
    see more 
    '''
    places_data = []        # name,number,addr
    for place in query_result.places:
        #print(place.name)
        #print(place.geo_location)
        #print(place.place_id)
        x = place.get_details()
        #print(place.vicinity)
        #print(place.local_phone_number)
        places_data.append([place.name,place.local_phone_number,place.vicinity])
    if len(places_data):
        return places_data[0]
        #print(place.details)

if __name__ == "__main__":
    retreive_area(loc="Mumbai, India",key="Hospitals")
