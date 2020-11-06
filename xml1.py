import xml.etree.ElementTree as ET
import requests

data = '''
<person>
<name>Misael</name>
<phone type = 'intl'>
    232524
</phone>
<email hide ='yes'/>
</person>
'''

users = '''
<stuff>
    <usuarios>
        <usuario x='2'>
            <name>Juan</name>
            <phone>8399439</phone>
            <email hide = 'yes'/>
        </usuario>
        <usuario x='5'>
            <name>Lara</name>
            <phone>7823929</phone>
            <email hide = 'yes'/>
        </usuario>
        <usuario x='6'>
            <name>Braian</name>
            <phone>8438394</phone>
            <email hide = 'no'/>
        </usuario>
    </usuarios>
</stuff>
'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))

print('\n\n')

datos = ET.fromstring(users)
lista = datos.findall('usuarios/usuario') 
print('User count: ', len(lista))

for u in lista:
    print("Usuario n°:"+ u.get('x'))
    print('Nombre: ' + u.find('name').text)
    print('Telefono: ' + u.find('phone').text)
    print('Atributo: ' + u.find("email").get('hide'))
    print('\n')