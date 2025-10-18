import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def __str__(self):
        return (f"{self.rekisteritunnus:6} | "
                f"Huippunopeus: {self.huippunopeus:3} km/h | "
                f"Nopeus: {self.nopeus:3} km/h | "
                f"Kuljettu matka: {self.kuljettu_matka:7.1f} km")

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


# --- Pääohjelma ---
autot = []
for i in range(1, 11):
    rek = f"ABC-{i}"
    huippu = random.randint(100, 200)
    autot.append(Auto(rek, huippu))

kilpailu_kaynnissa = True
tunti = 0

while kilpailu_kaynnissa:
    tunti += 1
    for auto in autot:
        muutos = random.randint(-10, 15)
        auto.kiihdyta(muutos)
        auto.kulje(1)
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False

# --- Tulostus ---
print(f"\nKilpailu päättyi {tunti} tunnin jälkeen!\n")
print(f"{'Auto':6} | {'Huippu':7} | {'Nopeus':7} | {'Matka (km)':10}")
print("-" * 45)
for auto in autot:
    print(f"{auto.rekisteritunnus:6} | {auto.huippunopeus:7} | "
          f"{auto.nopeus:7} | {auto.kuljettu_matka:10.1f}")
