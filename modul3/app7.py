lista = input("Introduceti lista de taskuri: ")
lista_taskuri = lista.split(" ")
print(lista_taskuri)

temp_list=[]
for i in lista_taskuri:
    if i not in temp_list:
        temp_list.append(i)

print(temp_list)
