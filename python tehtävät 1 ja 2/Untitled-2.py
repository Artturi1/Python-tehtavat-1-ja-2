









//1. Ohjelma, joka tervehtii nimelläsi

nimi = input("Anna nimesi: ")
print(f"Hei, {nimi}!")

//2. Ohjelma, joka laskee ympyrän pinta-alan

import math

sade = float(input("Anna ympyrän säde: "))
pinta_ala = math.pi * sade ** 2
print(f"Ympyrän pinta-ala on {pinta_ala:.2f}")

//3. Ohjelma, joka laskee suorakulmion piirin ja pinta-alan

kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print(f"Suorakulmion piiri on {piiri:.2f} ja pinta-ala on {pinta_ala:.2f}")


//4. Ohjelma, joka laskee lukujen summan, tulon ja keskiarvon

luku1 = int(input("Anna ensimmäinen kokonaisluku: "))
luku2 = int(input("Anna toinen kokonaisluku: "))

summa = luku1 + luku2
tulo = luku1 * luku2
keskiarvo = (luku1 + luku2) / 2

print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiarvo:.2f}")


//5. Ohjelma, joka muuntaa massan leivisköistä, nauloista ja luodeista kilogrammoiksi ja grammoiksi


# Muuntokertoimet
naula_kg = 0.425
leiviska_naulaa = 20
naula_luotia = 32
luoti_g = 13.3

# Syöte
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Laskenta
naulat_yht = leiviskat * leiviska_naulaa + naulat
luodit_yht = luodit + naulat_yht * naula_luotia
grammat_yht = luodit_yht * luoti_g

kg = int(grammat_yht // 1000)
g = grammat_yht % 1000

# Tulostus
print(f"\nMassa nykymittojen mukaan:\n{kg} kilogrammaa ja {g:.2f} grammaa.")


//6. Ohjelma, joka arpoo numerokoodeja


import random

# Kolminumeroinen koodi (väliltä 0-9)
koodi1 = ''.join(str(random.randint(0, 9)) for _ in range(3))
print("Kolminumeroinen koodi:", koodi1)

# Nelinumeroinen koodi (väliltä 1-6)
koodi2 = ''.join(str(random.randint(1, 6)) for _ in range(4))
print("Nelinumeroinen koodi:", koodi2)
