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
print(primes)

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


def modular_inverse(e,lcm):
    x = 0
    while True:
        if (e%lcm)*(x%lcm) % lcm == 1:
            return x
        x += 1
        

d = modular_inverse(e, lcm)

def encrypt(message):
    # message = [ord(c) for c in message]
    # message = 12
    encrypted_message = pow(12, e)%n
    return encrypted_message

print(encrypt('hi'))

def decrypt(message):
    decrypted_message = pow(12, d) % n
    return decrypted_message

m = decrypt(encrypt(12))
print(q, p, n, e, phi, d, m)