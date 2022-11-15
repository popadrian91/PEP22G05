# def adaugare():
#     nr_pruduse=int(input())
#     lista=[]
#     my_stoc={"Produs": "Produs", "Pret": "Pret", "Stoc": "Stoc"}
#     for i in range(nr_pruduse):
#         produs=input("Nume Produs")
#         pret=input("Pret")
#         stoc=input("Stoc")
#         stoc.update({"Produs": produs, "Pret": pret, "Stoc": stoc})
#     print(my_stoc)
#
# adaugare()

def adaugare_produs(stoc_existent: dict):
    prod=input("Introduceti produs: ")
    caract_produs = prod.split(";")
    stoc_existent.update({caract_produs[0]: [float(caract_produs[1]), int(caract_produs[2])]})
    #return stoc_existent

def stergere_produs(stoc_existent: dict):
    produs=input("Ce produs doresti sa stergi: ")
    del stoc_existent[produs]

def vizualizare_stoc(stoc_existent: dict):
    for produs, info in stoc_existent.items():
        print(f"{produs} : {info[1]}")

if __name__=="__main__":
    # vizualizare_stoc({"produs1": [3.5, 10]})
    # stergere_produs({"produs1": [3.5, 10]})
    adaugare_produs({"produs1": [3.5, 10]})

jssj