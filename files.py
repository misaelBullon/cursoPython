arch = input("Ingrese el nombre del archivo: ")
try:
    file = open(arch, 'r')
except:
    print("No se puede abrir el archivo")
    quit()

nLineas = 0
for linea in file:
   # print(linea)
    if linea.startswith('Misael'):
        linea = linea.rstrip() #Elimina la linea en blanco entre lineas
        print(linea)
    nLineas = nLineas + 1
print("El numero de lineas en el archivo es: "  ,nLineas)


    