import utils

def magazin():
    meniu= """
    Meniu:
1. Vizualizare stoc
2. Adaugare produs
3. Stergere produs
4. Iesire
"""
    stoc = {}
    while True:
        response=input(meniu).strip()
        if response=='1':
            utils.vizualizare_stoc(stoc)
        elif response=='2':
            utils.adaugare_produs(stoc)
        elif response=='3':
            utils.stergere_produs(stoc)
        elif response=='4':
            break
        else:
            print('Valoare invalida')

if __name__=="__main__":
    magazin()