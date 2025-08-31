
//4.1 Tulosta kaikki kolmella jaolliset luvut väliltä 1..1000
luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1
//4.2 Muunna tuumat senttimetreiksi, kunnes annetaan negatiivinen arvo
while True:
    tuumat = float(input("Anna tuumamäärä: "))
    if tuumat < 0:
        break
    cm = tuumat * 2.54
    print(f"{tuumat} tuumaa = {cm:.2f} cm")
//4.3 Syötä lukuja, kunnes tyhjä merkkijono, sitten tulosta pienin ja suurin
luvut = []

while True:
    syöte = input("Anna luku (tyhjä lopettaa): ")
    if syöte == "":
        break
    try:
        luku = float(syöte)
        luvut.append(luku)
    except ValueError:
        print("Virheellinen syöte, anna numero.")

if luvut:
    print(f"Pienin: {min(luvut)}, Suurin: {max(luvut)}")
else:
    print("Ei syötettyjä lukuja.")

//4.4 Arvauspeli (tietokone arpoo luvun 1..10)
import random

oikea_luku = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku (1-10): "))
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        break
//4.5 Kirjautuminen (max 5 yritystä, tunnus: python, salasana: rules)
yritykset = 0
while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if tunnus == "python" and salasana == "rules":
        print("Tervetuloa")
        break
    else:
        print("Väärä tunnus tai salasana")
        yritykset += 1
else:
    print("Pääsy evätty.")
//4.6 Monte Carlo -algoritmi π:n likiarvon laskemiseksi
import random

n = int(input("Kuinka monta pistettä arvotaan? "))
sisalla = 0
kokonaismaara = 0

while kokonaismaara < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        sisalla += 1
    kokonaismaara += 1

pi_likiarvo = 4 * sisalla / n
print(f"π likiarvo on: {pi_likiarvo}")
