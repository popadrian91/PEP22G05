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

carti()