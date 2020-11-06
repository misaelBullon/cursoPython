diccionario = {'a': 10, 'b': 15, 'c': 2}
archivo = open('intro.txt')

#imprimir la tupla ordenada
print(sorted([(v,k) for k,v in diccionario.items()]))
print(sorted([(k,v) for k,v in diccionario.items()]))

