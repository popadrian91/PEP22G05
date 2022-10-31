# Luati ca input un sir de la utilizator. Transformați șirul într-o lista și numarati vocalele din
# aceasta. Afisati numarul vocalelor pe consola.
# Introduceti un cuvant: Ananas
# Vocale in cuvantul dvs: 3

a = input('Sir: ')
a = a.lower()
b = list(a)
v = ['a', 'e', 'i', 'o', 'u']
c = 0
print(
    'Meniu: \n 1.Numar total de vocale \n 2.Numar de vocale individual')  # optiune 1 = numar total de vocale din string / optiune 2 = numar fiecare vocala in parte
z = input('Introduceti optiune: ')
if z == '1':
    for j in v:
        for i in b:
            if j == i:
                c = c + 1
    print('Vacale in cuvant :', c)
elif z == '2':
    # for j in v:
    #     vocala = b.count(j)
    #     if vocala !=0:
    #         print("Vocala ", j," se afla de " ,vocala,"ori")
    for j in v:
        for i in b:
            if j == i:
                c = c + 1
        if(c != 0):
            print('Vocala:', j, 'se regaseste de:', c, 'ori')
        c = 0
else:
    print('Optiune invalida. Bye Bye!')
