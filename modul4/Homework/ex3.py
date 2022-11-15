def carti():
    nr= input("Cate carti doriti sa adaugati in biblioteca?")
    lista_carti = []
    #dict={}
    for i in range(int(nr)):
        carte=input('Numele cartii: ')
        autor=input('Numele autorului: ')
        an=input('Anul publicarii: ')
        lista_carti.append({'nume': carte, 'autor': autor, 'an': an})
    print(lista_carti)
    an_publicare=input('anul publicarii dupa care doriti filtrare: ')
    for d in lista_carti:
        if d["an"] == an_publicare:
            #print(d['nume'], e['autore'], f['an'])
            print(d['nume'])
            #print('Exist')

carti()