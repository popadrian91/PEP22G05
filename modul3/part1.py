# a=100
# b=100
#
# if a > b:
#     print('a is larger')
# elif a>50:
#     print('a is grater then 50')
# elif a>60:
#     print('a is grater then 60')
# else:
#     print('b is larger')
#
#
# a = "101"
#
# if a > '100':
#     print('success')
# elif a == '100':
#     print('success ==')
#
# #chr() and ord()
#
# print(ord('0'))
# print(ord('1'))
# print(ord('a'))
# print(ord('A'))
#
# print(chr(65))
#
# # Trueish
#
# a = '101'
# print (a>'100')
#
# if True:
#     print('this will allways be true')
#
# if a:
#     print('this will also allways be true')
#
# a=""
# if a:
#     print('this will also allways be true')
# else:
#     print('a is False')
#
# a = -2 # orice numar diferit de 0 este adevarat si orice numar = cu 0 este fals
# if a:
#     print('a is True')
# else:
#     print('a is False')
#

#For loops

# a = 'my_string'
# a.__iter__()
# for i in a:
#     print(i)


# a = 100
# a.__iter__()
# for i in a:
#     print(i)


# result = range(10)
# print(result)
# print(type(result))
#
# print(result.__iter__())
#
# for i in result:
#     print(i)
#
# # while loop
# a=100
# while a<200:
#     print('inf')
#     a+=1
#     if a%2:
#         break

#continue

my_str = 'abcdefg'

# for letter in my_str:
#     print("before continue")
#     if letter == 'd':
#         continue #continue intrerupe executia in momentul in care este intalnit (this stop current ietration)
#     if letter == 'f':
#         break # this will stop for loop
#     print(letter)

# else keyword

for letter in my_str:
    print("before continue")
    if letter == 'd':
        continue #continue intrerupe executia in momentul in care este intalnit (this stop current ietration)
    # if letter == 'f':
    #     break # this will stop for loop
    print(letter)
else:
    print('all is done') # this is will never get exeuted if Breack is encountered


my_number=0

while my_number < 5:
    print(my_number)
    if my_number ==3:
        break
    my_number += 1
else:
    print('all done while')





