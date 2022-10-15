n=input('Introduceti un sir de caractere: ')
print('Enter dupa fiecare caracter este:\n','\n'.join(n[i:i + 1] for i in range(0, len(n), 1))) #splituire after each character using /n
print('Enter dupa fiecare caracter este:\n','\n'.join(n[i:i + 3] for i in range(0, len(n), 3))) #splituire after each character using /n

#print('Sirul introdus este: ', n,'\n' 'Sirul inversat este: ', n[::-1]) #print sir si sir inversat


