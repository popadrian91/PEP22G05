# functions
#3! = 1*2*3

# def factorial(number):
#     print(number)
#     result = 1
#     for i in range(1, number+1):
#         result *= i
#     return result
#
# result = factorial(10)
# print('Result is : ',result)


# def factorial(number, limit):
#     print(number)
#     result = 1
#     for i in range(1, number+1):
#         if result > limit:
#             return result #this stops functions execution
#         result *= i
#     return result
#
# result = factorial(100, 1000)
# print('Result is : ',result)

# variable number of arguments
def factorial(*args):
    print(args)

factorial(1,2,3)