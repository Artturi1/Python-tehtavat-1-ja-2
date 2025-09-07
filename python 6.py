import random
import math

//6.1
def heita_noppaa():
    return random.randint(1, 6)

def paohjelma1():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"Heitit: {silmaluku}")


//6.2

def heita_noppaa_tahkoilla(tahkot):
    return random.randint(1, tahkot)

def paohjelma2():
    tahkot = int(input("Anna nopan tahkojen määrä: "))
    maksimi = int(input("Anna suurin sallittu silmäluku: "))
    silmaluku = 0
    while silmaluku != maksimi:
        silmaluku = heita_noppaa_tahkoilla(tahkot)
        print(f"Heitit: {silmaluku}")
//6.3

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

def paohjelma3():
    while True:
        gallonat = float(input("Anna määrä (gallonoina, negatiivinen lopettaa): "))
        if gallonat < 0:
            break
        print(f"{gallonat} gallonaa = {gallonat_litroiksi(gallonat):.2f} litraa")


//6.4


def laske_summa(lista):
    return sum(lista)

def paohjelma4():
    luvut = [1, 2, 3, 4, 5]
    print(f"Lukujen summa: {laske_summa(luvut)}")


//6.5

def poista_parittomat(lista):
    return [luku for luku in lista if luku % 2 == 0]

def paohjelma5():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"Alkuperäinen lista: {luvut}")
    print(f"Parilliset: {poista_parittomat(luvut)}")
    '


//6.6

def pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    pinta_ala_m2 = math.pi * (halkaisija_cm / 200) ** 2  # halkaisija cm -> säde m
    return hinta_euro / pinta_ala_m2

def paohjelma6():
    d1 = float(input("Anna 1. pizzan halkaisija (cm): "))
    h1 = float(input("Anna 1. pizzan hinta (€): "))
    d2 = float(input("Anna 2. pizzan halkaisija (cm): "))
    h2 = float(input("Anna 2. pizzan hinta (€): "))

    y1 = pizzan_yksikkohinta(d1, h1)
    y2 = pizzan_yksikkohinta(d2, h2)

    print(f"1. pizzan yksikköhinta: {y1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {y2:.2f} €/m²")

    if y1 < y2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif y2 < y1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat ovat yhtä hyviä.")
