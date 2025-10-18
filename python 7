//7.1
vuodenajat = {
    "talvi": (12, 1, 2),
    "kevät": (3, 4, 5),
    "kesä": (6, 7, 8),
    "syksy": (9, 10, 11)
}

# Kysytään käyttäjältä kuukauden numero
kuukausi = int(input("Anna kuukauden numero (1–12): "))

# Etsitään oikea vuodenaika
for vuodenaika, kuukaudet in vuodenajat.items():
    if kuukausi in kuukaudet:
        print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan {vuodenaika}.")
        break


//7.2
# Luodaan joukko nimien tallentamiseen
nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)


//7.3

# Luodaan sanakirja lentokenttien tallentamiseen
lentoasemat = {}

while True:
    toiminto = input("Valitse toiminto (1=Uusi lentoasema, 2=Haku, Enter lopettaa): ")
    if toiminto == "":
        break

    if toiminto == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper()
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.\n")

    elif toiminto == "2":
        icao = input("Anna haettava ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[icao]}\n")
        else:
            print("Lentoasemaa ei löytynyt.\n")


