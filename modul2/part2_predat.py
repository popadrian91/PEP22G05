#String and String methods

my_var = 'Emanuel'
#U unicode
my_str = U"abcd"
print(my_str)
my_str = f"My name is {my_var}"
#f"" string formatabil ( continutul din obiectul paratezelor vor fi adaugate la string
print(my_str)
my_str = r"abcd {1} \n \{0}"
#r (row string, nu se interpreteaza backslesk din interiorul stringurilor
print(my_str)


my_str=my_str.capitalize()
print(my_str)

result=my_str.split('\\')
print(type(result))
print(result)
#split by default imparte dupa spatiu, intre paranteze se pune separator de split daca se vrea schimbarea acestuia


my_str=my_str.format('x','y')
print(my_str)


result=my_str.center(159)
print(result)


result='abd'.center(7,'#')
print(result)