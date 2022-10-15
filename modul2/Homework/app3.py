n1=input('Introduceti primul nume: ')
n2=input('Introduceti al 2-lea nume: ')
print('Lungimea primului nume este: ',len(n1), 'caractere') #lungimea primului nume
print('Cele 2 nume sunt la fel TRUE/FALSE:', n1==n2) #verificarea daca cele 2 numere sunt identice
print('Primul nume este mai lung TRUE/FALSE', n1>n2) #verificare daca primul nume este mai lung
print('Primul caracter al primului nume este: ', n1[0]) #print initiala primului nume
print('Primul nume inversat este: ', n1[::-1]) #primul nume inversat
n3=int(input('Introduceti valoarea de multiplicare a primului numar: '))
print('Primul nume multiplicat de ',n3,' este: ', n3*n1) #multiplicarea primului nume de n ori