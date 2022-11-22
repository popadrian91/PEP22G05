# generate prime numbers
import random


def primes(limit):
    result = []
    for i in range(2, limit):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


my_primes = primes(255)


# get 2 random prime number from list. Second number is smaller then first

# def get_primes(list_primes):
#     while True: # not goog solution
#         base = random.choice(list_primes)
#         if base < 129:
#             continue
#         else:
#             break
#     print(base)
#     return 1,2


def get_primes(list_primes):
    base_set = []
    prime_set = []
    for i in list_primes:
        if i >= 129:
            base_set.append(i)

    base = random.choice(base_set)
    for i in list_primes:
        if i < base:
            prime_set.append(i)
    prime = random.choice(prime_set)
    return base, prime


base, prime = get_primes(my_primes)
print(base)
print(prime)

def generate_local_secret(base):
    result = random.choice(range(2, base))
    return result

def generate_local_secret2(base):
    result = random.choice(range(2, base))
    return result

secret= generate_local_secret(base)

print(secret)

# this get's secret executed oon second PC
secret2= generate_local_secret2(base)
print(secret2)
def generate_remote_secret(base, prime, secret):
    result  = pow(prime, secret)%base
    return result


remote_secret = generate_remote_secret(base, prime, secret2)
print(remote_secret)

#this get's ececuted on first PC
local_secret = generate_remote_secret(base, remote_secret, secret)
print(local_secret)

#this get's executed on second PC
local_secret - generate_remote_secret(base, remote_secret, secret2)
print(local_secret)

common_local_secret = 121

#Text on first computer:
my_message = "My message to encrypt"
encrypted_resault = ''
for letter in my_message:
    encrypted_resault += (chr(ord(letter) ^ common_local_secret ))
print(encrypted_resault)

#Text on seccond computer:
decrypted_resaul = ''
for letter in encrypted_resault:
    decrypted_resaul +=chr(ord(letter)^common_local_secret)
print(decrypted_resaul)

