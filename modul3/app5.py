my_list=["Masa",5,"Scaun",4.5,[5,6,7],8]
for i in my_list:
    print('Tipul obiectului ',i ,'este: ',type(i))
    if type(i) == list:
        for j in i:
            print(type(j))
