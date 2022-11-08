# #import module
#
# import my_functions
# import time
# import math
# import random
# import sys
# print(sys.path)
# #sys.path.append("") daca se doreste update la path-urile de unde se importa module
# import modul4.part1
#
# print(type(random))
# result = random.random()
# print(result)
# result=random.randint(1, 5)
# print(result)
#
# result=time.time()
# print(result)
#
# time.sleep(1)
#
# from time import sleep
# print('before sleep')
# sleep(3)
# print('after sleep')
# # print(my_functions)
# # print(my_functions.factorial(6))

from my_functions import factorial

# my_imported_var='Local'
# from my_functions import *
# print(my_imported_var)

#import package

import my_package

print(type(my_package))
print(my_package.my_var)
print(my_package.factorial(10))

import test_package
print(test_package.suma())
