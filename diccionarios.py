diccionario = dict() #Constructor
diccionario["nombre"] = 'Misael'
diccionario["edad"] = 26
diccionario['sexo'] = 'Masculino'


print(diccionario) 

cuenta = dict()
names = ['Juan', 'Lara', 'Juan', 'Brainy', 'Anush', 'Juan', ]
for name in names:
    cuenta[name] = cuenta.get(name, 0) + 1
    #if name not in cuenta:
       # cuenta[name] = 1
   # else:
        #cuenta[name] = cuenta[name]+1

print(cuenta)

print(cuenta.keys()) #Accede a las claves del diccionario
print(cuenta.values())#Accede a los valores del diccionario
print(cuenta.items())#Devuelve una tupla con las key : values

for key,values in cuenta.items():
    print(key, values)


palabra = None
count = None

for p, c in cuenta.items():
    if count is None or c > count:
        palabra = p
        count = c
print(palabra, count)