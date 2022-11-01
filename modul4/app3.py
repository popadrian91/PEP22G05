# def dict():
#     empty_dic = {}
#     pc1_user = input('Introduceti utilizatorul PC-ului 1: ')
#     pc1_pass = input('Introduceti parola PC-ului 1: ')
#     pc2_user = input('Introduceti utilizatorul PC-ului 2: ')
#     pc2_pass = input('Introduceti parola PC-ului 2: ')
#     pc3_user = input('Introduceti utilizatorul PC-ului 3: ')
#     pc3_pass = input('Introduceti parola PC-ului 3: ')
#     empty_dic.update({pc1_user: pc1_pass,pc2_user: pc2_pass, pc3_user: pc3_pass})
#     print(empty_dic)
#     for key,passwd in empty_dic.items():
#         print(key ,'->', passwd)
#
#
# dict()

def calc():
    data = {}
    for i in range(1,4):
        user = input(f"Introduceti utilizatorul pc:{i}")
        parola = input(f"introduceti parola pc:{i}")
        data[user] = parola
    for key , value in data.items():
       print(user,'->',parola)
calc()