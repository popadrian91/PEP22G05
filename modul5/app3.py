def note():
    note=[]
    nume=input('Introduceti numele elevului')
    n=input('Introduceti notele elevului: ')
    note=n.split(",")
    print(note)
    if note:
        print("assert")
    lisa_note=[]
    for nota in note:
        try:
            lisa_note.append(int(nota))
        except ValueError:
            print("Introduceti cifre de la 1 la 10")
    p=0
    for i in lisa_note:
        p=p+i
    med=p/len(lisa_note)
    print(med)
    if med > 5:
        print(f"{nume} a trecut clasa cu media: {med}")
    else:
        print(f"{nume} a ramas repetent cu media {med}")


note()