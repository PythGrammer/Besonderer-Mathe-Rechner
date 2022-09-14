import EZLib
from EZLib import *

print("Bei Lineare Wachstums- und Abnahmemodelle darf keine Variable 0 sein!")
print("lzo und lk 3 Nummern und jz 1/2 Nummern!")
print("Falls Ergebnis gesucht wird einfach 0 eingeben!")
def lw(a,b,c):
    print("Original" + "\n" + "A = " + str(a) + "\n" + "B = " + str(b))
    a = a * c
    b = b * c
    print("\nMal c " + str(c) + "\nA = " + str(a) + "\n" + "B = " + str(b))
    return a, b

def la(a,b,c):
    print("Original" + "\n" + "A = " + str(a) + "\n" + "B = " + str(b))
    a = a * c
    b = b / c
    print("\nDurch c " + str(c) + "\nA = " + str(a) + "\n" + "B = " + str(b))
    return a, b

def lzo(t,km,e,c):
    print("Original\nZeit: " + str(t) + "\nEntfernung: " + str(km) + "\n")
    t = t * c
    km = e + km * c
    print("Mal " + str(c) + " Plus Entfernung " + str(e) + "\nZeit: " + str(t) + "\nEntfernung: " + str(km))
    return t, km

def lk(x,k,d,G):
    search = input("Was brauchst du? (G,x,k,d) ---> ")
    if(search == "G"):
        G = x * k + d
        print("G = " + str(G))
    elif(search == "x"):
        x = (G - d) / k
        print("x = " + str(x))
    elif(search == "k"):
        k = (G - d) / x
        print("k = " + str(k))
    elif(search == "d"):
        d = G - x * k
        print("d = " + str(d))
    else:
        print("Falscher Input!")
    return x, k, d, G

def jz(Z,K,p,pe):
    search = input("Was brauchst du? (Z,K,p,pe) ---> ")
    if(search == "Z"):
        Z = K * (p/100)
        print("Z = " + str(Z))
    elif(search == "K"):
        K = Z / (p/100)
        print("K = " + str(K))
    elif(search == "p"):
        p = Z / K * 100
        print("p = " + str(p))
    elif(search == "pe"):
        pe = 0.75 * p
        print("pe = " + str(pe))
    else:
        print("Falscher Input!")
    return Z, K, p, pe

running = True
while running == True:
    action = input("Was willst du machen? (lw,la,lzo,lk,jz,aus) ---> ")
    if(action == "lw"):
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        c = int(input("Mal wieviel?: "))
        lw(a,b,c)
    elif(action == "la"):
        a = int(input("Number 1: "))
        b = int(input("Number 2: "))
        c = int(input("Mal wieviel?: "))
        la(a,b,c)
    elif(action == "lzo"):
        t = int(input("Zeit: "))
        km = int(input("Entfernung in Zeit: "))
        e = int(input("Entfernung vom Ausgangspunkt: "))
        c = int(input("Mal wieviel?: "))
        lzo(t,km,e,c)
    elif(action == "lk"):
        x = int(input("Menge: "))
        k = int(input("Kosten pro x: "))
        d = int(input("Fixkosten: "))
        G = int(input("Gesamtkosten: "))
        lk(x,k,d,G)
    elif(action == "jz"):
        Z = int(input("Zinsen: "))
        K = int(input("Kapital: "))
        p = int(input("Zinsensatz: "))
        pe = int(input("Effektiver Zinsensatz: "))
        jz(Z,K,p,pe)
    elif(action == "aus"):
        EZLib.exit(running)
    else:
        print("Falscher Input!")
