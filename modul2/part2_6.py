a='Hello Python'
b='Ana are mere'
c='Pizza partty'

print (a.replace(" ", "_"))
print (b.replace(" ", "_"))
print (c.replace(" ", "_"))

result = a.split()
print(result[0] , result[1], sep='_')
result1 = b.split()
print(result1[0] , result1[1], sep='_')
result2 = c.split()
print(result2[0] , result2[1], sep='_')

print(a+'.')
print(b+'.')
print(c+'.')

print(result[0] * 4)
print(result1[0] * 4)
print(result2[0] * 4)


# a = 'Hello Python'
# b = 'Ana are mere'
# c = 'Pizza Party'
# result = a.split()
# print(result[0], result[1], sep='_')
# print(a.split()[0], a.split()[1], b.replace(' ', '_'), c, sep='_')
# print(a.split()[0], a.split()[1], b.replace(' ', '_'), c, '.',sep='_')
# print(a + '.', b.replace(' ', '_'), c, '.',sep='_')
# print(a.split()[0]*4, a.split()[1], b.replace(' ', '_'), c, sep='_')


x,y = a.split()
print(x, y)
print(x)