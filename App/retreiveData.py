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
    location='Andheri,Mumbai', keyword='Hospitals',
        radius=2000,types=[types.TYPE_HOSPITAL])
    '''
    see more 
    '''
    for place in query_result.places:
        print(place.name)
        print(place.geo_location)
        print(place.place_id)
        x = place.get_details()
        print(place.vicinity)
        print(place.local_phone_number)
        #print(place.details)

if __name__ == "__main__":
    retreive_area(loc="Mumbai, India",key="Hospitals")
