parola=7788

b=range(3)
for i in b:
    a = int(input('Introduceti o parola: '))
    if(a==parola):
        print('Acces permis')
        break
    else:
        print('Parola gresita. mai incercati.')
else:
    print('Acccount locked')