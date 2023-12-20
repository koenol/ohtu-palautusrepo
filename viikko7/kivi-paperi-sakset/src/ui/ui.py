from services.kivi_paperi_sakset import KPS

class UI:
    def __init__(self):
        self.pelimodit = {
            "a": KPS.kaksinpeli,
            "b": KPS.tekoaly_helppo,
            "c": KPS.tekoaly_vaikea
        }

    def __str__(self):
        print("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )
    def _kaynnista_peli(self, pelivalinta):
        peli = self.pelimodit[pelivalinta]()

        while True:
            siirrot = ["k", "p", "s"]

            siirto1 = input("Ensimmäisen pelaajan siirto: ")
            if siirto1 not in siirrot:
                break
            peli.pelaaja1.aseta_siirto(siirto1)

            if pelivalinta == "a":
                siirto2 = input("Toisen pelaajan siirto: ")
                if siirto2 not in siirrot:
                    break
                peli.pelaaja2.aseta_siirto(siirto2)
            peli.pelaa()
            if pelivalinta != "a":
                print(f"Tietokone pelasi: {peli.pelaaja2.hae_siirto()}")

    def kaynnista(self):
        while True:
            self.__str__()
            
            pelivalinta = input()
            if pelivalinta in self.pelimodit:
                self._kaynnista_peli(pelivalinta)
            else:
                break
