def reidicare_la_putere(a,b):
    return int(a)**int(b)


def num():
    while True:
        data=input('Introduceti 2 val despartite de virgula')
        if data == 'q':
            break
        a,b=data.split(",")
        print('Result is: ', reidicare_la_putere(a,b))


result=num()