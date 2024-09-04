import urllib
import requests

while True:
    pokemon = input("Which pokemon do you want  to find ?")
    pokemon = pokemon.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    req = request.get(url)
    if req.status_code == 200:
        data = req.json()
        print("\t Name : \t {data['name']}")
        print("\t Abilities :")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("\t ---------    Pokemon not found !   ---------")