import urllib.request, urllib.parse, urllib.error
import json

serviceUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input("Ingrese su direccion: ")
    if len(address) < 1: break

    url = serviceUrl + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('Failure to retrieve')
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]

    print('lat', lat, 'lng' , lng )

    location = js['results'][0]['formated_adrress']
    print(location)