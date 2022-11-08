import random


def funtie():
    i = 0
    while i < 5:
        i = i + 1
        my_ran=[]
        my_list=[]
        for j in range(6):
            num = random.randint(0, 49)
            my_ran.append(num)
        print(my_ran)

        a=0
        while len(my_list)<=5:
            #a = int(input('Introduceti o valoare: '))
            try:
                a = int(input('Introduceti o valoare: '))
                if a > 49:
                    print('Valoarea iese din range, alege valoare intre 0 si 49, mai ai ', 5 - i, 'incercari')
                else:
                    my_list.append(a)
            except ValueError:
                print('valoare introdusa este incorecta')
        print(my_list)

        for j in my_list:
            if j in my_ran:
                print(f"Felicitari numarul {j} este castigator")
        if my_ran == my_list:
            print('Felicitari ai ghicit toate numerele')
            break
        elif (5 - i) == 0:
            print('Nu mai ai incercari, mai cumpara o fisa')
        elif (5 - i) >= 1:
            print(f"Mai incearca, mai ai {5 - i} incercari")

funtie()