# Luati ca input un sir de la utilizator. Transformați șirul într-o lista și numarati vocalele din
# aceasta. Afisati numarul vocalelor pe consola.
# Introduceti un cuvant: Ananas
# Vocale in cuvantul dvs: 3

a=input('Sir: ')
a=a.lower()
b=list(a)
v=['a','e','i','o','u']
print(b)
c=0
for j in v:
    for i in b:
        if j==i:
            c=c+1
print('Vacale in cuvant :',c)