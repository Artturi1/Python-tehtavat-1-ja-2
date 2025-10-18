class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

    def siirry_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.kerros_ylos()
        while self.nykyinen > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.hissit = [Hissi(alin, ylin) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissin_nro, kohde):
        print(f"\nAjetaan hissiä {hissin_nro+1}:")
        self.hissit[hissin_nro].siirry_kerrokseen(kohde)

    def palohälytys(self):
        print("\nPalohälytys! Kaikki hissit pohjakerrokseen:")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin)
