#continue

#my_str = 'abcdefg'

# for letter in my_str:
#     print("before continue")
#     if letter == 'd':
#         continue #continue intrerupe executia in momentul in care este intalnit (this stop current ietration)
#     if letter == 'f':
#         break # this will stop for loop
#     print(letter)

# else keyword

# for letter in my_str:
#     print("before continue")
#     if letter == 'd':
#         continue #continue intrerupe executia in momentul in care este intalnit (this stop current ietration)
#     # if letter == 'f':
#     #     break # this will stop for loop
#     print(letter)
# else:
#     print('all is done') # this is will never get exeuted if Breack is encountered
#
#
# my_number=0
#
# while my_number < 5:
#     print(my_number)
#     if my_number ==3:
#         break
#     my_number += 1
# else:
#     print('all done while')
#


# list

#obicete care ne permit sa salvam in interiorul lor referinte catre alte obiecte
# my_var = 3.3
# my_list = ['a',1,True,my_var]
#
# my_list.__iter__()
#
# for obj in my_list:
#     print(obj)
#
# print('adding to list')
# my_list.append([])
# for obj in my_list:
#     print(obj)
#
# print(f'first object is : {my_list[0]}')
# print(f'second object is : {my_list[1]}')
# print(f'third object is : {my_list[2]}')
# print(f'forth object is : {my_list[3]}')
# print(f'fifth object is : {my_list[-1]}')
#
# print('Response is: ',my_list.extend([1,2,3]))
# for obj in my_list:
#     print(obj)
#
# print(my_list)
#


#modifyng object
# a = "name: {}"
# print('Initial ID:',id(a))
# resault = a.format('abcd')
# print(id(a))
# print(id(resault))
# print(a)
#
# b = ["name: {}"]
# print('Initial ID:',id(b))
# resault = b.append('abcd')
# print(id(b))
# print(id(resault))
# print(b) #lists are mutable

#mutable object in modifyng for loop

my_new_list=list('random')
# for letter in my_new_list:
#     my_new_list.append('a')
#     print(letter)

# for letter in my_new_list:
#     my_new_list.pop()
#     print(letter)

for letter in my_new_list.copy(): #copy of the list
    my_new_list.pop()
    print(letter)
print(my_new_list)