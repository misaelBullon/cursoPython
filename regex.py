import re

# ^ ---> Encuentra el comienzo de una linea
# $ ---> Encuentra el fin de una linea
# . ---> Encuentra un caracter
# \s ---> Encuentra un espacio en blanco
# \S ---> Encuentra cualquier caracter que no sea espacio en blanco
# * ---> Repite un caracter 0 (cero) o mas veces
# *? ---> Repite un caracter cero o mas veces (non-greedy)
# + ---> Repite un caracter una o mas veces
# +? ---> Repite un caracter una o mas veces (non-greedy)
#[aeiou] ---> Encuentra cualquier caracter dentro de la lista
#[^XYZ] ---> Ecuantra cualquier caracter que no se encuentre dentro de la lista
#[a-z0-9]---> Encuentra cualquier caracter dentro del rango de la lista
#() ---> Indica donde comienza y donde termina la extracción de un string


archivo = open('intro.txt', 'r')
for line in archivo:
    line = line.rstrip()
    if re.search('^could', line):
        print(line)

data = 'From misa.esteban@gmail.com sabado 5 ene 16:45 2020'

match = re.findall('@[^ ]*', data) #re.findall('From .^@([^ ]*))
print(match)

