diccionario = dict()
lista = list()
listaGrande = list()
nuevoDiccionario = dict()

archivo = open('intro.txt', 'r')
for linea in archivo:
    linea = linea.rstrip()
    lista = linea.split()
    for palabra in lista:
        listaGrande.append(palabra)

for palabra in listaGrande:
    diccionario[palabra] = diccionario.get(palabra, 0) + 1


cuenta = None
word= None

for clave, valor in diccionario.items():
    if cuenta is None or valor > cuenta:
        cuenta = valor
        word = clave
        nuevoDiccionario[clave] = valor

#-----------Buscar palabra mas usada----------

print("Palabra mas usada en el archivo")
print(word, cuenta)
print("\n")

#------Buscar las palabras mas usadas en el archivo-------

newlist = list()
for k,v in diccionario.items():
    tupla = (v,k)
    newlist.append(tupla)
newlist = sorted(newlist, reverse=True)

print("Lista de las 5 palabras mas usadas en el archivo")
for k,v in newlist[:5]:
    print(k,v)