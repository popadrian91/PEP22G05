# 1. Declarați o listă care conține următoarele elemente: [‘abc’,123,’1’,1].
# - afișarea tipului fiecărui element din lista
# - Aflarea numărului numerelor întregi, numerelor float, respectiv a șirurilor din lista

lista=['abc',123,'1',1]
my_str=0
my_int=0
my_float=0
for i in lista:
    print('Tipului elementului',i,'este :',type(i))
    if  type(i)== str:
        my_str+=1
    if type(i) == int:
        my_int+=1
    if type(i)== float:
        my_float+=1
print('Number of str: ',my_str)
print('Number of int: ',my_int)
print('Number of float: ',my_float)