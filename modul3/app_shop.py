shop1 = {'apples': 7.5, 'plumps': 8.3, 'bread':3.5}
shop2 = {'apples': 7.6, 'plumps': 8.1, 'bread':3.5}
shop3 = {'apples': 7.4, 'plumps': 8.9, 'bread':3.5}

shopping_cart = {'apples': 3, 'plumps': 5, 'bread':4}
shops = {'lid': shop1, 'kau': shop2, 'pro': shop3}

#what is the cheapest shop
# for i in shop1.keys():
#     for j in shopping_cart:
#         a = shop1['apples'] * shopping_cart['apples']
#         b= shop1['plumps'] * shopping_cart['plumps']
#         c= shop1['bread'] * shopping_cart['bread']
#         d=a+b+c
#
# for i in shop2.keys():
#     for j in shopping_cart:
#          aa = shop2['apples'] * shopping_cart['apples']
#          bb= shop2['plumps'] * shopping_cart['plumps']
#          cc= shop2['bread'] * shopping_cart['bread']
#          dd=aa+bb+cc
#
# for i in shop3.keys():
#     for j in shopping_cart:
#          aaa = shop3['apples'] * shopping_cart['apples']
#          bbb= shop3['plumps'] * shopping_cart['plumps']
#          ccc= shop3['bread'] * shopping_cart['bread']
#          ddd=aaa+bbb+ccc
#
# print(d,dd,ddd)
#
# shops.update({'lid': d, 'kau': dd, 'pro': ddd})


result={}

for shop_name, shop in shops.items():
    for product , quantity in shopping_cart.items():

        if result.get(shop_name):
            result.update({shop_name: (shop[product] * quantity) + result[shop_name]})
        else:
            result.update({shop_name: shop[product] * quantity})

print(result)
print(min(result.values()))