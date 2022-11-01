# variables in funtion

#global variables in functions

# my_var = "Emanuel"
#
# def print_data():
#     global my_var
#     my_var = 'NewName'
#     my_local = 'Local'
#     print(f'Global {my_var}')
#
#     def new_print_data():
#         nonlocal my_local
#         my_local='modified local'
#         print(f'In second funtion local:  {my_local}')
#         print(f'In second funtion {my_var}')
#     new_print_data()
#     print('Local var in first function : ', my_local)
#
#
# print(f'outside global {my_var}')
# print(f'outside global {my_var}')
# print_data()

# """
# Create app that is able to respond  with the provided name
#
# Hi Bob,
# >>> My name is Jhon
# Hi Jhon,
#
#
# All of this will be in a function
#
# """


# def robot():
#     name = 'Bob'
#
#     def functie():
#         nonlocal name
#         print('Hi', name)
#         name = input('My name is ')
#         print('Hi ', name)
#
#     functie()
#
#     def weather():
#         vreme = input('How is the weather')
#         print("For ", name, "the weather is ", vreme.split()[-1])
#
#     weather()
#
# robot()

my_tupple = (1,2,3)
print(my_tupple)

my_tupple = 1,2,3
print(my_tupple)
print(type(my_tupple))

a = 5
b = 3
a, b =b,a
print(a,b)

#unpack variables in tuple

a=5
b=3
c=7
d = 11
a,b,c,d=d,c,b,a
print(a,b,c,d)
a,*var,d =d,c,b,a
print(a,d)
print(var)

def test_function(*args, **kwargs):
    print('Args',args)
    print('KWARGS',kwargs)

test_function(1,2,3, end='\n', next=(123,))