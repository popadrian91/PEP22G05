#binery char
# 10 = 0000 1010 binar
# 10 = 0     A hexa
# 10 = 0     12

print(ord('a'))
print(ord('A'))

a_number = ord('a')
A_number = ord('A')
print(bin(A_number))
print(bin(a_number))

print(max('abcd'))
print(max('AabcdZ!'))

letter1 = chr(70)
letter2 = chr(32)

print(letter1, letter2)

print ( (10 ^ 25) ^ 25 )

print(80*"#")
my_message= "This is my message"
encrypted_resault = ''
for letter in my_message:
    encrypted_resault += (chr(ord(letter) ^ 48 ))
print(encrypted_resault)

decrypted_resaul = ''
for letter in encrypted_resault:
    decrypted_resaul +=chr(ord(letter)^48)
print(decrypted_resaul)

