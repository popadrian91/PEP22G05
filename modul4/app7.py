a = """In primavara anului 1894, toata Londra a fost interesata, iar lumea la moda a fost consternata de
uciderea onorabilului Ronald Adair in circumstante cele mai neobisnuite si inexplicabile. Publicul
a aflat deja acele detalii ale crimei care au iesit la iveala in ancheta politiei; dar multe au fost
suprimate cu acea ocazie, deoarece cazul acuzarii era atat de coplesitor de puternic, incat nu era
necesar sa se prezinte toate faptele. Abia acum, la sfarsitul a aproape zece ani, imi este permis sa 
aprovizionez acele verigi lipsa care alcatuiesc intregul lant remarcabil. Crima era interesanta in sine, dar acel interes nu era nimic pentru mine in comparatie cu continuarea de neconceput, care
mi-a oferit cel mai mare soc si surpriza din orice eveniment din vitța mea aventuroasa. Chiar si 
acum, dupa acest interval lung, mă trezesc emotionat cand ma gandesc la asta si simt din nou acel
potop brusc de bucurie, uimire si neincredere care mi-a cufundat cu totul mintea."""

a=a.lower()
def count_litera():
    b=list(a)
    c=input('Introduceti o litera: ')
    for i in b:
        count=b.count(c)
    print(f"Litera introdusa se regaseste de: {count} ori")

def split_to_list():
    global my_list
    my_list= a.split(" ")
    print(f"Lista alcatuita din cuvinte este: {my_list}")

def new_list():
    my_empty_list = []
    for i in my_list:
        if i[0]=='s':
            my_empty_list.append(i)
    print(f"Cuvintele care incep cu s sunt {my_empty_list}")


count_litera()
split_to_list()
new_list()