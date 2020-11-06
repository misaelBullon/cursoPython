my_str = "Hola Mundo"
#print(dir(my_str))


#Extraer porcion de texto ingresado
correo = input("Ingrese su correo electrónico: ")
pArroba = correo.find('@')

pPunto = correo.find('.', pArroba)

servidor = correo[pArroba + 1 : pPunto]

print("Su servidor de correo electronico es: " + servidor)