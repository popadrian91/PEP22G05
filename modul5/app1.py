import random
def joc():
    state={'p': 'piatra', 'f': 'foarfeca', 'h': 'hartie'}

    result = {'piatra-foarfeca': True, 'foarfeca-hartie': True, 'hartie-piatra': True}
    options = list(state.keys())
    nume=input('Introduceti numele: ')

    op = input('Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), q pentru a iesi]: ')
    if op == 'g':
        print('Quit')
        quit()
    else:
        selection = random.randint(0,2)
        selected = options[selection]
        print(selected)
    if op not in options:
        print('Optiune invalida')

    print(f'> {nume}: {state[op]}')
    print(f'>Server : {state[selected]}')

    # if op == 'p' and selected == 'h':
    #     print('Server')
    # elif op == 'p' and selected == 'p':
    #     print('Remiza')
    # elif op == 'p' and selected == 'f':
    #     print(nume)
    # elif op == 'h' and selected == 'h':
    #     print('Remiza')
    # elif op == 'h' and selected == 'p':
    #     print('Remiza')
    # elif op == 'h' and selected == 'f':
    #     print('Server')
    # elif op == 'f' and selected == 'h':
    #     print(nume)
    # elif op == 'f' and selected == 'f':
    #     print('Remmiza')

    if state[op]== state[selected]:
        print('Remiza')
        return None
    try:
        result[f'{state[op]}--{state[selected]}']
        print('Ai castigat !')
    except:
        print('Serverul a castigat !')

joc()
    # while True:
    #
    #     op=input('Introduceti optiunea [p (piatra),f (foarfeca) ,h (hartie), qpentru a iesi]: f')
    #     ran=random.randint(0,3)
    #     if ran ==1:
    #         op_new="piatra"
    #     elif ran ==2:
    #         op_new="foarfeca"
    #     elif ran==3:
    #         op_new="hartie"
    #
    #     if op="piatra" and op_new=""
