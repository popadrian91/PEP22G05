def factorial(limit):
    result = 1
    for i in range(1, limit+1):
        result *= i
    return result

my_imported_var = 'imported'
print(__name__)
print(__package__)
if __name__ == "__main__":
    print(__name__) # variabila __name__ exista in orice modul de python si contine
    print('Print from module: ',factorial(5))