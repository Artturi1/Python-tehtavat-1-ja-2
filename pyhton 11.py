
//11.1
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"Julkaisu: {self.nimi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}\n  Kirjoittaja: {self.kirjoittaja}\n  Sivumäärä: {self.sivumaara}\n")


class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}\n  Päätoimittaja: {self.paatoimittaja}\n")


# Pääohjelma
aku_ankka = Lehti("Aku Ankka", "Aki Hyypiä")
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti6.tulosta_tiedot()



//11.2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = max(0, min(self.nopeus + muutos, self.huippunopeus))

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akku_kapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akku_kapasiteetti = akku_kapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki


# Pääohjelma
sahko = Sahkoauto("ABC-15", 180, 52.5)
bensa = Polttomoottoriauto("ACD-123", 165, 32.3)

sahko.kiihdyta(100)
bensa.kiihdyta(120)

sahko.kulje(3)
bensa.kulje(3)

print(f"Sähköauto {sahko.rekisteritunnus}: {sahko.kuljettu_matka} km")
print(f"Polttomoottoriauto {bensa.rekisteritunnus}: {bensa.kuljettu_matka} km")
