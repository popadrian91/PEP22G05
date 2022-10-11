a=int(input('Venit-ul lunar este:'))
ch=int(input('Procentul Cheltuielilor: '))
re=int(input('Procentul recreeri: '))
ec=int(input('Procentul economiilor: '))
cheltuieli =(ch *a)/100
recreere= (re * a)/100
economii = (ec * a)/100
print('Venit: ',a)
print('Cheltuieli:', cheltuieli)
print('Recreere: ', recreere)
print('Economii: ',economii)