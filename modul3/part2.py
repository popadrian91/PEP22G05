#continue

my_str = 'abcdefg'

# for letter in my_str:
#     print("before continue")
#     if letter == 'd':
#         continue #continue intrerupe executia in momentul in care este intalnit (this stop current ietration)
#     if letter == 'f':
#         break # this will stop for loop
#     print(letter)

# else keyword

for letter in my_str:
    print("before continue")
    if letter == 'd':
        continue #continue intrerupe executia in momentul in care este intalnit (this stop current ietration)
    # if letter == 'f':
    #     break # this will stop for loop
    print(letter)
else:
    print('all is done') # this is will never get exeuted if Breack is encountered


my_number=0

while my_number < 5:
    print(my_number)
    if my_number ==3:
        break
    my_number += 1
else:
    print('all done while')



