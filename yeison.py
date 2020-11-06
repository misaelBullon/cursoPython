import json

data = '''
{
    "name" : "Misael",
    "telefono": {
        "type" : "intl",
        "number" : "893483"
    },
    "email":{
        "direccion" : "msnfvodnv@nonrv",
        "hide" : "yes"
    }
}
'''

info = json.loads(data)

print('Name: ' , info["name"])
print('telefono: ', info["telefono"]["number"])
print('Hide: ' , info["email"]["hide"])
print('\n')

datos = ''' 
[
    {
        "name" : "Misael",
        "direccion" : "89jdfjnj@nonrv",
        "hide" : "yes"
    },
    {
        "name" : "Juan",
        "direccion" : "983jfkvdnd@nonrv",
        "hide" : "yes"
    },
    {
        "name" : "Brian",
        "direccion" : "0'0kofv v@nonrv",
        "hide" : "yes"
    }
]
'''

informacion = json.loads(datos)
for d in informacion:
    print('Name: ' , d["name"])
    print('Email: ' , d["direccion"])
    print('\n')

