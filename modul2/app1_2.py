"""
reverse a and b

"""

a=4
b=5

c =a
a = b
b = c

a, b =b, a
print (a ,b)

a = a ^ b
b = a ^ b
a = a ^ b
print (a ,b)