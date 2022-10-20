print('Cappuccino ...4 lei')
print('Espresso ...3.5 lei')
# while True:
#     a = int(input('Ce optiune alegeti? [1,2]'))
#     if(a==1 or a==2):
#         break
a = int(input('Ce optiune alegeti? [1,2]'))
while not(1<=a<3):
    a=int(input('Optiune invalida, alegeti optiune dintre 1 si 2'))


b = int(input('Introduceti o bancnota[5,10]: '))
p=0

if(a==1):
    p=4
elif(a==2):
    p=3.5

if(b==5 or b==10):
    print('Veti primi restul de ', b-p)
    print('Produsul se livreaza')
else:
    print('Bancnota invalida')