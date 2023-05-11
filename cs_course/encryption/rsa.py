import random
import math


"""rsa functionality - https://www.javatpoint.com/rsa-encryption-algorithm

implementation help - https://www.geeksforgeeks.org/rsa-algorithm-cryptography/

generation of prime numbers - https://stackoverflow.com/questions/16091581/how-many-prime-numbers-are-there-available-for-rsa-encryption"""


def primefinder(n: int) -> list[int]:
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = True

    for i in range(2, math.isqrt(n)):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]

primes = primefinder(1000)
# print(primes)

# p = 993481
# q = 848017

p = 11
q = 13

n = p*q

phi = (p-1)*(q-1)

def coprime(e, phi):
    while e < phi:
        if math.gcd(e, phi) == 1:
                return e
        e += 1

e = coprime(2, phi)

lcm = math.lcm(p-1, q-1)

# def extended_euclidean_algorithm(e, phi):
#     l = []
#     factor = e
#     result = phi
#     while True:
#         amount = math.floor(phi/factor)
#         rest = phi % factor

#         l.append([result, amount, factor, rest])
#         phi = factor
#         result = phi
#         factor = rest
#         if rest == 1:
#             break
    
#     while True:
#         pass
        
# def extended_gcd(a, b):
#     if a == 0:
#         return b, 0, 1
#     else:
#         gcd, x, y = extended_gcd(b % a, a)
#         return gcd, y - (b // a) * x, x


# print(extended_gcd(3, 3127))

# d = extended_gcd(11, 701111)[1] + 701111

# print(d)

# def modular_inverse(e,lcm):
#     x = 0
#     while True:
#         if (e%lcm)*(x%lcm) % lcm == 1:
#             return x
#         x += 1
        

# d = modular_inverse(e, lcm)

from typing import Tuple
def xgcd(a: int, b: int) -> Tuple[int, int, int]:
    
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

d = xgcd(11, 349716)[1] + 349716

print(d)

def encrypt(message):
    # message = [ord(c) for c in message]
    # message = 12
    encrypted_message = pow(12, e)%n
    return encrypted_message

# print(encrypt('hi'))

def decrypt(message):
    decrypted_message = pow(12, d) % n
    return decrypted_message

# m = decrypt(encrypt(12))
# print(q, p, n, e, phi, d, m)