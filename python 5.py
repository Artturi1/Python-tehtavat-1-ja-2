//5.1 Arpakuutioiden silmälukujen summa
import random

n = int(input("Kuinka monta arpakuutiota heitetään? "))
summa = 0

for i in range(n):
    heitto = random.randint(1, 6)
    print(f"Heitto {i+1}: {heitto}")
    summa += heitto

print(f"Silmälukujen summa on {summa}")
//5.2. Viisi suurinta lukua

luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)
//5.3. Onko luku alkuluku?

    luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    on_alkuluku = False
else:
    on_alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")
//5.4. Kaupunkien nimet listaan ja tulostus samassa järjestyksessä

kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("\nKaupungit annetussa järjestyksessä:")
for kaupunki in kaupungit:
    print(kaupunki)
