from googleplaces import GooglePlaces, types, lang
import sys
from config import *
import googlemaps,re
from datetime import datetime


YOUR_API_KEY = "AIzaSyAlKXS0K2tTl3a2wFeDmuzESqrFG-OVKpw"

google_places = GooglePlaces(YOUR_API_KEY)

type_map = {
    "HOSPITAL":types.TYPE_HOSPITAL,
    "CHEMIST":types.TYPE_PHARMACY,
    "POLICE":types.TYPE_POLICE,
    "TRAIN":types.TYPE_TRAIN_STATION,
    "TAXI":types.TYPE_TAXI_STAND,
    "GAS":types.TYPE_GAS_STATION,
    "ATM":types.TYPE_ATM
    }

'''
# TEXT_SEARCH
query_result = google_places.text_search(query="Restaurant in Dahisar",location="Mumbai,India",radius=2000)

# AUTOCOMPLETE
query_result = google_places.autocomplete(input="Dahisar w",location="Mumbai,India",radius=200)
print(query_result.predictions)
'''

# print(dir(types))
# NEARBY AREA SEARCH

def google_directions(ori, dest, mo):
    message = []
    gmaps = googlemaps.Client(key='AIzaSyB8eWNRDQSrDaHtSyiHmm1eLOYW4bM4QtI')
    now = datetime.now()
    directions_result = None
    print(ori,dest,mo)
    try: 
        directions_result = gmaps.directions(origin=ori, destination=dest,mode=mo, departure_time = now)
    except:
        print("A network error occurred; please try again")
    
    if directions_result == None:
        print("An error occurred; please check your inputs and try again")
    message.append("Start from: " + directions_result[0]['legs'][0]['start_address'])
    message.append("End at: " + directions_result[0]['legs'][0]['end_address'])
    message.append("Duration: " + directions_result[0]['legs'][0]['duration']['text'])
    message.append("Distance: " + directions_result[0]['legs'][0]['distance']['text'])
    
    regex = re.compile('<[^>]*>')
    style_regex = re.compile('<[^>]*(style)[^>]*>')
    for each in directions_result[0]['legs'][0]['steps']:
        instr = re.sub(style_regex, '; ', each['html_instructions'])
        instr = re.sub(regex, '', instr)
        message.append(instr)
    return '\n'.join(message)

def process_detail(bod):
    message = 'No search term' 
    params = {'lang': 'en'}
    if bod[bod.index('detail')+7:] != "":
        inp = bod.splitlines()
        if len(inp) > 2:
            params['term'] = inp[2]
        resp = client.search(inp[1], **params)
        if resp != None:
            bus = resp.businesses[0]
            message = '\n' + bus.name + '\nPhone: ' + bus.display_phone + '\nAddress: ' + '\n'.join(bus.location.display_address) + '\n' + str(bus.rating) + '/5 over ' + str(bus.review_count) + ' reviews'
    return message



def retreive_area(loc,key,type):
    # temps here
    print("Retreiving data")
    query_result = google_places.nearby_search(location=loc, keyword=key, radius=2000, types=[type_map[key]])
    places_data = []        # name,number,addr
    for place in query_result.places:
        # print(place.place_id)
        x = place.get_details()
        places_data.append([place.name,place.local_phone_number,place.vicinity])
    if type == "nearby":
        if len(places_data):
            return places_data[0]
    if type == "route":
        x = "Dahisar anand nagar" 
        y = "Kamothe Sector 34"
        print(google_directions(x,y,mo="transit"))
        #print(google_directions(places_data[0][-1],key,mo="transit"))

if __name__ == "__main__":
    retreive_area(loc="Dahisar ,Mumbai",key="POLICE",type="route")
