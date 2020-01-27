# Coding=UTF-8
import secrets
from math import sqrt
import time
from tkinter import *

janela = Tk()

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
This function receives the text do encrypt
the E and n numbers
and encrypt the text
'''
def encrypt(text, E, n):
    lenght = len(text)
    text = text.lower()#Converting message to lower case, so we don't need other 2 dictionaries
    binary = bin(E).replace("0b", "")
    binn = list(binary)
    binn.reverse()
    bin_list = []
    i = 0
    for c in binn:
        if c == "1":
            bin_list.append(pow(2, i))
            i += 1
        elif c == "0":
            i += 1
    i = 0
    encrypted = ""
    while i < lenght:
        if not text.isdigit():
            letter = text[i]  # Only one letter at time
            aux = catalougue[letter]
            index = fast_exponenciation(bin_list, n, 1, aux % n, 1)#Conversion and concating in string
            encrypted = encrypted + str(index)
            if i + 1 != lenght:
                encrypted += " "
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
    binary = bin(d).replace("0b","")
    binn = list(binary)
    binn.reverse()
    bin_list = []
    i = 0
    for c in binn:
        if c == "1":
            bin_list.append(pow(2, i))
            i += 1
        elif c == "0":
            i += 1
    i = 0
    #print(bin_list)
    #print("AUGUSTINHO CARRARA")
    while i < lenght:
        aux = ""
        while i < lenght and Encrypted[i] != ' ':#Verifying if the next position of message is a ','
            aux += Encrypted[i]
            i += 1
        i += 1
        #print(aux)
        aux = int(aux)
        index = fast_exponenciation(bin_list, n, 1, aux % n, 1)
        decrypted += catalougue2[index]
    return decrypted

'''
Extended version of euclidean algorithm to calculate the modular inverse
'''
def Extended_Euclidean_Algorithm(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = Extended_Euclidean_Algorithm(b % a, a)
        return g, x - (b // a) * y, y

'''
Function that calculates the inverse, to decrypt the message
'''
def inverse(a, m):
    g, x, y = Extended_Euclidean_Algorithm(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



def Totient(): #GUI function to generate the key in a txt

        x = int(e3.get())

        e3.destroy()
        b1.destroy()
        label.destroy()

        label1 = Label(janela, text= "Done!", bg = "black")
        label1.config(font=("Courier", 35), fg = "white")
        label1.place(x = 180, y = 150)
               
        p_key = n, x


        try:#Public Key writed on an archive
            archive = open('Public Key.txt', 'r+')
            archive.writelines(str(p_key))
            archive.close()
        except FileNotFoundError:#If the archive not exist/not found, create another archive
            archive = open('Public Key.txt', 'w+')
            archive.writelines(str(p_key))
            archive.close()
    


def Generate_PK():

    p = int(e1.get())
    q = int(e2.get())

    global n
    n = p * q
    totient = phi_function(p, q)

    lab.destroy()
    e1.destroy()
    e2.destroy()
    b.destroy()
   

    global label
    label = Label(janela,text = "Insert a value E / mcd(E,phi) = 1", bg = "black")
    label.config(font=("Courier", 15), fg = "white")
    label.place(x = 50, y = 150)

    global e3
    e3 = Entry(janela)
    e3.place(x = 150, y = 200)

    global b1
    b1 = Button(janela, text = "OK",command = Totient)
    b1.place(x = 150, y = 250)

        


def input_PK():#GUI page for Genarate Public Key Option

    l.destroy()
    l2.destroy()
    btn.destroy()
    btn2.destroy()
    btn3.destroy()

    global lab

    lab = Label(janela, text = "Insert two prime numbers P and Q:", bg = "black")
    lab.config(font=("Courier", 15), fg = "white")
    lab.place(x = 50, y = 150)
    
    global e1
    e1 = Entry(janela)
    e1.place(x = 150, y = 200)
    global e2
    e2 = Entry(janela)
    e2.place(x = 150,  y = 250)
    global b
    b = Button(janela, text = "OK",command = Generate_PK)
    b.place(x = 150, y = 300)


def gui_Encrypt():


    msg1 = msg.get()    #Message
    z = int(k.get())    #n
    z1 = int(k1.get())  #e

    la.destroy()
    msg.destroy()
    la2.destroy()
    k1.destroy()
    k.destroy()
    w.destroy()

    label1 = Label(janela, text= "Done!", bg = "black")
    label1.config(font=("Courier", 35), fg = "white")
    label1.place(x = 180, y = 150)

    Encrypted = encrypt(msg1, z1, z)
    try:
        archive = open('Encrypted Message.txt', 'r+')
        archive.writelines(str(Encrypted))
        archive.close()
    except FileNotFoundError:
        archive = open('Encrypted Message.txt', 'w+')
        archive.writelines(str(Encrypted))
        archive.close()



def input_Encrypt():#GUI page for Encrypt Messa option
    l.destroy()
    l2.destroy()
    btn.destroy()
    btn2.destroy()
    btn3.destroy()

    global la
    la = Label(janela, text = "Insert here your message to encrypt", bg = "black")
    la.config(font=("Courier",15), fg = "white")
    la.place(x = 50, y = 100)

    global msg
    msg = Entry(janela)
    msg.place(x = 150, y = 150)


    global la2
    la2 = Label(janela, text = "Insert the Public Key", bg = "black")
    la2.config(font=("Courier",15),fg = "white")
    la2.place(x = 140, y = 200)

    global k
    k = Entry(janela)
    k.place(x = 150, y = 250)


    global k1
    k1 = Entry(janela)
    k1.place(x = 150, y = 300)

    global w
    w = Button(janela, text = "OK", command = gui_Encrypt)
    w.place(x = 150, y = 350)


def gui_Decrypt():
    xp1 = int(xp.get())
    xq1 = int(xq.get())
    xe1 = int(xe.get())

    xn = xp1 * xq1
    Encrypted = ""

    xp.destroy()
    xq.destroy()
    xlab.destroy()
    xlab1.destroy()
    xbut.destroy()
    xe.destroy()

    xlab2 = Label(janela, text = "Done!", bg = "black")
    xlab2.config(font=("Courier",35), fg = "white")
    xlab2.place(x = 180, y = 150)

    
    try:
        archive = open('Encrypted Message.txt', 'r+')
        for nb in archive:
            Encrypted = Encrypted + nb
        archive.close()
    except FileNotFoundError:
        raise Exception('The file with encrypted message not exists')


    totient = phi_function(xp1, xq1)
 
    d = inverse(xe1, totient)
    start = time.time()
    text = decrypt(Encrypted, xn, d)
    end = time.time()
    try:
        archive = open('Decrypted Message.txt', 'r+')
        archive.writelines(text)
        archive.close()
    except FileNotFoundError:
        archive = open('Decrypted Message.txt', 'w+')
        archive.writelines(text)
        archive.close()



def input_Decrypt():#GUI page for Decrypt Message option
    l.destroy()
    l2.destroy()
    btn.destroy()
    btn2.destroy()
    btn3.destroy()


    global xlab
    xlab = Label(janela, text = "Type P and Q again(P first then Q)", bg = "black")
    xlab.config(font=("Courier",15), fg = "white")
    xlab.place(x = 50, y = 100)

    global xp
    xp = Entry(janela)
    xp.place(x = 150, y = 150)

    global xq
    xq = Entry(janela)
    xq.place(x = 150, y = 200)

    global xlab1
    xlab1 = Label(janela, text = "Type E :", bg = "black")
    xlab1.config(font=("Courier",15), fg = "white")
    xlab1.place(x = 150, y = 250)

    global xe
    xe = Entry(janela)
    xe.place(x = 150, y = 300)

    global xbut
    xbut = Button(janela, text = "OK", command = gui_Decrypt)
    xbut.place(x = 150, y = 350)



#first page of GUI------------------------------------------

janela.title("RSA Enigma Encrypter")

janela.geometry("500x500+200+200")
janela.resizable(0,0)
#janela.iconbitmap("icon.ico")
janela['bg'] = "black"

#labels
l = Label(janela,text = "Welcome to the RSA enigma encrypter!", bg = "black")
l.config(font=("Courier", 15), fg = "white")
l.place(x = 50, y = 100)
#----
l2 = Label(janela,text = "Please, select the action", bg = "black")
l2.config(font=("Courier", 11), fg = "white")
l2.place(x = 140, y = 130)
#----

#botoes

btn = Button(janela,text = "Generate public key", bg = "white", command = input_PK)
btn.config(height = 1, width = 18, font = ("Courier",10))
btn.place(x = 170, y = 200)


btn2 = Button(janela,text = "Encrypt message", bg = "white", command = input_Encrypt)
btn2.config(height = 1, width = 18, font = ("Courier",10),)
btn2.place(x = 170, y = 250)


btn3 = Button(janela,text = "Decrypt message", bg = "white", command = input_Decrypt)
btn3.config(height = 1, width = 18, font = ("Courier",10))
btn3.place(x = 170, y = 300)



janela.mainloop()
