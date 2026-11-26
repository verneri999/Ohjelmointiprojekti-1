class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    # Tallentaa pelaajan tiedot pelaaja.txt-tiedostoon
    def tallenna(self):
        with open("pelaaja.txt", "a") as tiedosto:
            tiedosto.write(self.nimi + "\n")
            tiedosto.write(str(self.ika) + "\n")

#kysyy iän
def kysy_ika():
    while True:
        try:
            ika = int(input("Ikä: "))
        except ValueError:
            print("Anna ikä numerona.")
            continue

        if ika < 12:
            print("et voi pelata")
            exit()
        return ika

def ohjeet():
    print("Pelin ohjeet...")

def aloita_peli(pelaaja):
    print("")

#päävalikon vaihtoehdot
def paavalikko(pelaaja):
    while True:
        print()
        print("1. Uusi peli")
        print("2. ohjeet")
        print("3. Aijemmat tulokset")
        print("4. lopeta")
        valinta = input("Valitse: ")

        if valinta == "1":
            aloita_peli(pelaaja)
        elif valinta == "2":
            ohjeet(pelaaja)


nimi = input("Nimi: ")
ika = kysy_ika()

pelaaja = Pelaaja(nimi, ika)
pelaaja.tallenna()
print("Tervetuloa!", pelaaja.nimi)
paavalikko(pelaaja)

