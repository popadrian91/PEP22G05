def functie():
    global x
    x=int(input())
    if x >= 10 and x <= 20 :
        x = 3*(x)**2 -4*(3*x) + 4
       # y = 3*x
        print(x)

functie()