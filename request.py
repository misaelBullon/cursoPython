import requests

def getPokemon(url = 'http://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset': offset} if offset else{} #Si offset es distinto de 0, sino manda un diccionario vacio
    response = requests.get(url, params=args)
    if response.status_code == 200:
        payload = response.json()
        results = payload.get('results', [])
        if results:
            for pokemon in results:
                nombre = pokemon['name']
                print(nombre)
            next = input('Continuar listando? [Y/N]').lower()
            if next == 'y':
                getPokemon(offset=offset+20)

getPokemon()

