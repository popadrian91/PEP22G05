# Output functions
print('Hello World')

#Input functions
#a=input('Say Hello: ')
#print('Hello ' + a)

# Variabless
my_name = 'Adi'
print(my_name)
#my_number = 1000000
#my_number = 1_000_000
my_number = 1000_000
print(my_number)


#type functions
result = type(10)
print (result)

#return of print
result=print('exemple')
print(result)

#return of input
#result=input('Say Hello: ')
#print(result)


#print multiple args
print('Emanuel', 'Ion', 'Ilie')

#casting
# result = 'abcd'
# result = int(result)

# Operatii

# comparation
a = "abcd"
b = "abcd"
print(a==b)
print('ID of a is: ', id(a))
print('ID of b is:' , id(b))
print(a is b)



#slice
a ="my_text"
print(a[1])
print(a[1:3])
print(a[1:7])
print(a[1:])
print(a[:6])
print(a[:])

print(a[:6:2]) #ultimul 2 reprezinta pasul

    #-7-6-5-4-3-2-1
a ='my_text'
print(a[-1])
print(a[-6:-1])
print(a[-1:-6:-1]) #la pas negativ merge de la dreapta la stanga

b = 'This is may reversed text'
print(b[::-1])