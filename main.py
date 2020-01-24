# Coding=UTF-8
import secrets
from math import sqrt
import time

catalougue = {'a':2, 'b':3,'c':4,'d':5,'e':6,'f':7,'g':8,'h':9,'i':10,'j':11,'k':12,'l':13,'m':14,'n':15,'o':16,'p':17,'q':18,'r':19
              , 's':20,'t':21,'u':22,'v':23,'w':24,'x':25,'y':26,'z':27,' ':28}
catalougue2 = {2:'a', 3:'b', 4:'c', 5:'d', 6:'e', 7:'f', 8:'g', 9:'h', 10:'i', 11:'j', 12:'k', 13:'l', 14:'m', 15:'n', 16:'o', 17:'p'
               , 18:'q', 19:'r', 20:'s', 21:'t', 22:'u', 23:'v', 24:'w', 25:'x', 26:'y', 27:'z', 28:' '}

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
def are_coprimes(a, b, x, y, flag):
    if a == 0:
        x = 0
        y = 1
        return b
    x1 = 1
    y1 = 1  # Store the recusive results
    mcd = are_coprimes(b % a, a, x1, y1, flag)
    # updating x and y with the recursive results
    x = y1 - (b / a) * x1
    y = x1
    if flag != 0:
        return mcd
    else:
        return x

'''
Euler's totient function
'''
def phi_function(p, q):
    if (is_prime(p) and is_prime(q)):#Both parameters have to be two prime numbers
        return (p - 1) * (q - 1)

'''
Function that receives the n number
and calculates a random E number that is prime
'''
def make_E(n):
    e = secrets.randbits(12)#Generating an random E with 12 bits
    if are_coprimes(e, n, 1, 1, 1):
        return e
    else:
        e = make_E(n)
    return e

'''
Function that makes a random prime number
'''
def mk_primes():
    while True:
        prime = secrets.randbits(12)#Generating a random prime with 12 bits
        if is_prime(prime):
            return prime

'''
Function to calculate the fast modular exponentiation
'''
def fast_modular_exponentiation(aux, E, n):
    r = 1
    if 1 and E:
        r = aux
    while E:
        E >>= 1
        aux = (aux * aux) % n
        if E and 1:
            r = (r * aux) % n
    return r

'''
This function receives the text do encrypt
the E and n numbers
and encrypt the text
'''
def encrypt(text, E, n):
    lenght = len(text)
    text = text.lower()#Converting message to lower case, so we don't need other 2 dictionaries
    i = 0
    encrypted = ""
    while i < lenght:
        letter = text[i]#Only one letter at time
        encrypted = encrypted + str(fast_modular_exponentiation(catalougue[letter],E,n))#Conversion and concating in string
        if i + 1 != lenght:
            encrypted += ","
        i += 1
    return encrypted

'''
Another fast modular exponenciation function
'''
def fast_exponenciation(bin_list, n, i, y, z):
    if i > int(bin_list[-1]):
        return z % n
    else:
        if i in bin_list:
            z = z * y
            #print(z)
        return fast_exponenciation(bin_list, n, i * 2, (y * y) % n, z)

'''
Function to convert the inverse into binary
facilitates the processing
'''
def con_bin(num):
    if num == 1:
        return "1"
    else:
        r = str(num % 2)
        return r + con_bin(num // 2)

'''
This function receives the encrypted text
n key and d key, and decrypt the message
'''
def decrypt(Encrypted, n, d):
    lenght = len(Encrypted)
    decrypted = ""
    binary = con_bin(d)
    bin_list = []
    i = 0
    for c in binary:
        if c == "1":
            bin_list.append(pow(2, i))
            i += 1
        elif c == "0":
            i += 1
    i = 0
    print(bin_list)
    #print("AUGUSTINHO CARRARA")
    while i < lenght:
        aux = ""
        while i < lenght and Encrypted[i] != ',':#Verifying if the next position of message is a ','
            aux += Encrypted[i]
            i += 1
        i += 1
        #print(aux)
        aux = int(aux)
        index = fast_exponenciation(bin_list, n, 1, aux % n, 1)
        decrypted += catalougue2[index]
    return decrypted

'''
Function that calculates the inverse, to decrypt the message
'''
def inverse(a, m):
    m0 = m
    y = 0
    x = 1
    if (m == 1):
        return 0
    while (a > 1):
        # q is quotient
        q = a // m
        t = m
        # m is remainder now, process same as Euclid's algorithm
        m = a % m
        a = t
        t = y
        # Update x and y
        y = x - q * y
        x = t
        # Make x positive
    if x < 0:
        x = x + m0
    return x

def main():
    while True:
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
            print("Insert two prime numbers P and Q:")
            while True:
                p = int(input())#User have to insert an P prime number
                q = int(input())#User have to insert an Q prime number
                if is_prime(p) and is_prime(q):#This while is only breaked when the both numbers are primes
                    break
            n = p * q
            totient = phi_function(p, q)
            while True:
                print("Insert a value E / mcd(E, Phi) = 1")
                e = int(input())#User have to insert an E number that are coprime to Totient
                if are_coprimes(e, totient, 1, 1, 1):#E have to be coprime to the totient
                    break
            p_key = n, e
            try:#Public Key writed on an archive
                archive = open('Public Key.txt', 'r+')
                archive.writelines(str(p_key))
                archive.close()
            except FileNotFoundError:#If the archive not exist/not found, create another archive
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
            Encrypted = input()
            totient = phi_function(p, q)
            #print("oi sumido")
            d = inverse(e, totient)
            #print("bye")
            start = time.time()
            text = decrypt(Encrypted, n, d)
            end = time.time()
            print(end - start)
            try:
                archive = open('Decrypted Message.txt', 'r+')
                archive.writelines(text)
                archive.close()
            except FileNotFoundError:
                archive = open('Decrypted Message.txt', 'w+')
                archive.writelines(text)
                archive.close()
        elif option == 4:
            exit()

main()