import urllib.request, urllib.parse, urllib.error

myUrl = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in myUrl:
    words = line.decode().strip()
    print(words)