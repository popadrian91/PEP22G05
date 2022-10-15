cuv=input('Introduceti un cuvant: ')
print('Cuvantul introdus este: ', cuv)
cuv_nou=cuv.upper() #transformarea la tot cuvantul in upper case
cuv_inv=cuv_nou[::-1] #cuvant inverat

print('Cuvantul este palindrom: ', cuv_nou==cuv_inv) #print cuvantul este palindrom TRUE/FALSE
