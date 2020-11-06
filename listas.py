lista = ['dnvnd', [1,2], 3.4]
for i in lista:
    print(i)

nuevaLista = list() #Crea lista con el constructor

nuevaLista.append('5')
nuevaLista.append('2')
nuevaLista.sort() #Ordena la lista de menor a mayor

for dato in nuevaLista:
    print(dato)

nl = list()
valor = ''
while(valor != 'done'):
    valor = input("Por favor ingrese un valor: ")
    if valor == 'done':
        break
    else:
        nl.append(float(valor))
promedio = sum(nl)/len(nl)

print(promedio)

#-----Patrón guardián-----
#   if len(dato) < 1:
 #    continue