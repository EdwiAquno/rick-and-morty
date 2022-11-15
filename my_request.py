from wsgiref import headers
import requests
url = 'https://rickandmortyapi.com/api/character'

payload={}
headers={}

response = requests.request("GET",url, headers=headers, data=payload)
 #print(response.json())

respuesta_json =response.json()
#print(respuesta_json['info'])
#print(respuesta_json['results'])
info =respuesta_json['info']
personajes = respuesta_json['results']
#for name in respuesta_json['results']:
  #print(name['name'])
for personaje in personajes:
    print(f"el personaje{personaje['name']} esta {personaje['status']}")  