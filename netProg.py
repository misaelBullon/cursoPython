import socket
import urllib.request, urllib.parse, urllib.error

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Se crea el objeto socket conectado a traves de internet y que recibe un flujo de datos
mysock.connect(('data.pr4e.org', 80))


cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysock.close()


myUrl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in myUrl:
    print(line.decode().strip())