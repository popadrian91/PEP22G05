lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(" ")
print(lista_taskuri)

lista_taskuri = list(dict.fromkeys(lista_taskuri))
print(lista_taskuri)