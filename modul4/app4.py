angajat1 = {
'nume': 'Ana-Maria Popescu',
'departament': 'IT',
'ID': 3409,
'Salar': 4560,
}
angajat2 = {
'nume': 'Marian Muntean',
'departament': 'IT',
'ID': 2235,
'Salar': 4556,
}
angajat3 = {
'nume': 'Maria Manea',
'departament': 'HR',
'ID': 1908,
'Salar': 6755,
}
angajat4 = {
'nume': 'Oana Popa',
'departament': 'HR',
'ID': 1977,
'Salar': 5400,
}
angajat5 = {
'nume': 'David Codru',
'departament': 'Management',
'ID': 1988,
'Salar': 12900,
}
lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]

#print(lista_dict)

# for i in lista_dict:
#     if i['Salar'] > 5000:
#         print(i['nume'],i['departament'],i['ID'])
#
# lista_new=list()
# for i in lista_dict:
#     if i['departament'] != ['Management']:
#         #print(i['nume'])
#         #lista_new=[i['nume']]
#         lista_new.append(i['nume'])
# print(lista_new)
#
#
#


lista_dict = [angajat1, angajat2, angajat3, angajat4, angajat5]
lista_angajati = []
lista_salar = []
for angajat in lista_dict:
    if angajat['Salar'] > 5000:
        print(f" {angajat['nume']} -> {angajat['departament']}")
    # Creați o lista cu numele angajatilor, mai puțin a managerului, si afisati-o.
    if angajat['departament'] != 'Management':
        lista_angajati.append(angajat['nume'])
    # Faceti media salariala pe departamentul HR si afisati-o.
    if angajat['departament'] == 'HR':
        lista_salar.append(angajat['Salar'])
print("Angajati:")
for nume in lista_angajati:
    print(" - ", nume)
media = sum(lista_salar) / len(lista_salar)
print(f"Media HR = {media}")
