parola=7788
i=0
#b=range(3)
while i<3:
    i +=1
    a = int(input('Introduceti o parola: '))
    if(a==parola):
        print('Acces permis')
        break
    else:
        print('Parola gresita. mai incercati.')
else:
    print('Acccount locked')