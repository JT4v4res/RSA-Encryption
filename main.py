# Coding=UTF-8
import secrets
from math import sqrt

'''
This function receives a number x
and checks if he's a prime number
'''


def is_prime(x):
    square_root = sqrt(x)
    c = 0
    for i in range(2, x):
        if x == 2:
            break
        elif x % 2 == 0:
            c += 1
            break
        elif x % i == 0:
            c += 1
            break
        elif i > square_root:
            break
    if c == 0:
        return True
    else:
        return False


'''
This function receives two values a, b 
and calculate the Max Common Divisor between then
using the Euclidean Algorithm
'''


def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
This function receives four numbers a, b, x, y
and checks if a, b are coprimes numbers
using the extended version of the Euclidean Algorithm
'''


def are_coprimes(a, b, x, y):
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1  # Store the recusive results
    mcd = are_coprimes(b % a, a, x1, y1)
    # updating x and y with the recursive results
    x = y1 - (b / a) * x1
    y = x1
    return mcd


'''
Euler's totient function
'''


def phi_function(p, q):
    if (is_prime(p) and is_prime(q)):
        return (p - 1) * (q - 1)


'''
Function that receives the n number
and calculates a random E number that is prime
'''


def make_E(n):
    e = secrets.randbits(12)
    if are_coprimes(e, n, 1, 1):
        return e
    else:
        e = make_E(n)
    return e


'''
Function that makes a random prime number
'''


def mk_primes():
    while True:
        prime = secrets.randbits(12)
        if is_prime(prime):
            return prime


'''
This function receives the text do encrypt
the E and n numbers
and encrypt the text
'''


def encrypt(text, E, n):
    lenght = len(text)
    text = text.lower()
    i = 0
    encrypted = []
    while i < lenght:
        if text[i] != ' ':
            aux = ord(text[i]) - 95
        else:
            aux = ord(text[i]) - 4
        aux = aux ** E
        d = aux % n
        encrypted.append(d)
        i += 1
    return encrypted


'''
This function receives the encrypted text
n key and d key, and decrypt the message
'''


def decrypt(Encrypted, n, d):
    decrypted = []
    i = 0
    lenght = len(Encrypted)
    [int(element) for element in Encrypted]
    while i < lenght:
        aux = Encrypted[i] ** d
        text = aux % n
        letter = chr(text + 95)
        decrypted.append(letter)
        i += 1
    return decrypted


def get_private_key(Phi, e):
    d = 0
    while (are_coprimes(d * e, Phi, 1 ,1 ) != 1):
        d += 1
    return d


def main():
    print("--------------------------------")
    print("Welcome to RSA enigma encrypter!")
    print("--------------------------------")
    print("Please, select the action")
    print("1 - Generate public key")
    print("2 - Encrypt message")
    print("3 - Decrypt message")
    print("4 - Exit")
    print("--------------------------------")
    option = int(input())
    if option == 1:
        print("Select the action")
        print("1 - Generate random P, Q and E numbers")
        print("2 - Use yours P, Q and E numbers")
        print("--------------------------------------")
        second_option = int(input())
        if second_option == 1:
            p = mk_primes()
            print(p)
            q = mk_primes()
            print(q)
            n = p * q
            e = make_E(n)
            p_key = n, e
            try:
                archive = open('Public Key.txt', 'r+')
                archive.writelines(str(p_key))
                archive.close()
            except FileNotFoundError:
                archive = open('Public Key.txt', 'w+')
                archive.writelines(str(p_key))
                archive.close()
        elif second_option == 2:
            p = int(input())
            q = int(input())
            n = p * q
            e = int(input())
            p_key = n, e
            try:
                archive = open('Public Key.txt', 'r+')
                archive.writelines(str(p_key))
                archive.close()
            except FileNotFoundError:
                archive = open('Public Key.txt', 'w+')
                archive.writelines(str(p_key))
                archive.close()
    elif option == 2:
        print("Insert here your message to encrypt")
        text = input()
        print("-----------------------------------")
        print("Insert here the public key")
        print("Type N")
        n = int(input())
        print("Type E")
        e = int(input())
        Encrypted = encrypt(text, e, n)
        try:
            archive = open('Encrypted Message.txt', 'r+')
            archive.writelines(str(Encrypted))
            archive.close()
        except FileNotFoundError:
            archive = open('Encrypted Message.txt', 'w+')
            archive.writelines(str(Encrypted))
            archive.close()
    elif option == 3:
        print("Type P and Q again(P first then Q)")
        p = int(input())
        q = int(input())
        print("Type E")
        e = int(input())
        n = p * q
        print("Type the encrypted Message")
        Encrypted = []
        Encrypted.append(int(input()))
        totient = phi_function(p, q)
        d = get_private_key(totient, e)
        text = decrypt(Encrypted, n, d)
        try:
            archive = open('Decrypted Message.txt', 'r+')
            archive.writelines(str(text))
            archive.close()
        except FileNotFoundError:
            archive = open('Decrypted Message.txt', 'w+')
            archive.writelines(str(text))
            archive.close()
    elif option == 4:
        exit()

main()