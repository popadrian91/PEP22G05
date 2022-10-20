a=input('Introduceti primele 7 cifre din CNP')
an=a[1:3]
a=a[1]
luna=a[3:5]
zi=a[5:]
print(an, luna, zi)

if(int(a) == 0):
    an='20'+an
elif(int(a)== 1):
    an='21'+an
elif(int(a)==2):
    an='22'+an
else:
    an='19'+an

print(an)

if(2022-int(an)>18):
    print('Major')
else:
    print('Minor')