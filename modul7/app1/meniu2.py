from app import Haine
from app import Accesorii

produse = []
h1 = Haine("Pantaloni", 100, 3)
a1 = Accesorii("Bratara", 100, "argint", 4)
produse.append(h1)
produse.append(a1)

def vizualizare(produse):
    for produs in produse:
        print(produs)

def add_product():
    products = {'1': Haine, '2':Accesorii}
    product_selector= input("What is the category: \n 1: Haine \n 2: Accesorii")
    nume=input('Name: ')
    pret = int(input('Price: '))
    stoc = int(input('stock: '))
    if product_selector==2:
        material=input('Material: ')
    else:
        material=None
    try:
        new_product = products[product_selector](nume,pret,stoc, material=material)
    except:
        print('something is wrong')
    produse.append(new_product)
    # if a==1:
    #     prod=input("Nume produs: ")
    #     if prod != None:
    #         pret=input("Pret")
    #         if pret != None:
    #             stoc = input("Stoc: ")
    # produse.append(prod,pret,stoc)




def meniu():
    meniu = {"1": add_product, "2": vizualizare, "3": quit}
    while True:
        optiune = input("Optiuni:\n 1.Adaugare produs\n 2.Vizualizati\n 3.Iesire\n").strip()
        try:
            if optiune == "2":
                meniu[optiune](produse)
            if optiune == "1":
                meniu[optiune]
        except KeyError:
            print("Incorrect value! try again... ")

meniu()
#add_product()


#
# def prt():
#     print(str(bluze))
#     print(str(cercei))
#
#
# def meniu():
#     while True:
#         men = input('====PRODUSE===== \n 1.Adaugare Produs \n 2.Vizualizare Produs \n 3.Iesire la medniul Principal \n')
#         men = int(men)
#         if men == 2:
#             prt()
#
#
# meniu()
