class Kurssi:
    def __init__(self, nimi, vuosi):
        self.__nimi = nimi
        self.__vuosi = vuosi
        self.__palautteet = []
        try:
            with open(nimi + ".csv") as tiedosto:
                for rivi in tiedosto:
                    osat = rivi.split(";")
                    self.__palautteet.append({
                        "opiskelija": osat[0], 
                        "arvosana": int(osat[1]), 
                        "kommentti": osat[2]
                    })
        except:
            pass

    def tarkista_palautteen_antaja(self, palaute):
        for x in self.__palautteet:
            if x["opiskelija"] == palaute["opiskelija"]:
                return True
            
    def lisaa_palaute(self, palaute):
        self.__palautteet.append({
            "opiskelija": palaute.get("opiskelija"),
            "arvosana": palaute.get("arvosana"),
            "kommentti": palaute.get("kommentti", "")
        })

    def tallenna_csv_tiedostoon(self):
        with open(self.__nimi + ".csv", "w") as tiedosto:
            for p in self.__palautteet:
                tiedosto.write(f"{p['opiskelija']};{p['arvosana']};{p['kommentti']};\n")

    def anna_palaute(self, uusi_palaute):
        if not self.tarkista_palautteen_antaja(uusi_palaute):
            self.lisaa_palaute(uusi_palaute)
            self.tallenna_csv_tiedostoon()
            return True

    def muuta_palautetta(self, muutettu_palaute):
        for x in self.__palautteet:
            if x["opiskelija"] == muutettu_palaute["opiskelija"]:
                x["kommentti"] = muutettu_palaute["kommentti"]

                self.tallenna_csv_tiedostoon()
                return True

        return False
    
    def hae_palaute(self, opiskelija):
        for p in self.__palautteet:
            if p["opiskelija"] == opiskelija:
                return p

        return None
    
    def hae_kommentin_sisaltavat_palautteet(self):
        palautteet = []
        for palaute in self.__palautteet:
            if len(palaute["kommentti"]) > 0:
                palautteet.append(palaute)
        
        return palautteet

    def hae_palautteet_joiden_arvosana(self, x):
        palautteet = []
        for palaute in self.__palautteet:
            if palaute["arvosana"] == x:
                palautteet.append(palaute)
        
        return palautteet

    def hae_palautteet_joiden_arvosana_valilla(self, x, y):
        palautteet = []
        for palaute in self.__palautteet:
            if palaute["arvosana"] >= x and palaute["arvosana"] <= y:
                palautteet.append(palaute)
        
        return palautteet

    def hae_kaikki_arvosanat(self):
        arvosanat = []
        for x in self.__palautteet:
            arvosanat.append(int(x["arvosana"]))
        return sum(arvosanat)
    
    def hae_palautteiden_maara(self):
        palautteet = 0
        for x in self.__palautteet:
            palautteet += 1
        return palautteet

    def tulosta_keskiarvo(self):
        keskiarvo = self.hae_kaikki_arvosanat() / len(self.__palautteet)
        print(f"kurssin keskiarvo: {keskiarvo}")

    def hae_arvosanojen_maara(self, arvosana):
        arvosanat = 0
        for x in self.__palautteet:
            if x["arvosana"] == arvosana:
                arvosanat += 1
        return arvosanat

    def tulosta_jakauma(self):
        print(f"\njakauma:")
        for i in range(5, 0, -1):
            tahdet = self.hae_arvosanojen_maara(i)
            print(f"{i}: {tahdet * '*'}")

    def tulosta_kommentit(self):
        print("\n" + "kommentit")
        for palaute in self.__palautteet:
            if len(palaute["kommentti"]) > 0:
                print("  " + palaute["kommentti"])

    def yhteenveto(self):
        print(f"{self.__nimi}, {self.__vuosi}")
        print("============")
        print("palautteita annettiin", len(self.__palautteet), "kappaletta")
        self.tulosta_keskiarvo()
        self.tulosta_jakauma()
        self.tulosta_kommentit()


# testipääohjelma
ohtu = Kurssi("ohtu", 2023)
ohtu.anna_palaute({ "opiskelija": "01234567", "arvosana": 4, "kommentti": "hyvät laskarit" })
ohtu.anna_palaute({ "opiskelija": "01234567", "arvosana": 2, "kommentti": "paska koe" })
ohtu.muuta_palautetta({ "opiskelija": "01234567", "arvosana": 2, "kommentti": "paska koe" })
ohtu.anna_palaute({ "opiskelija": "01231221", "arvosana": 4 })
ohtu.anna_palaute({ "opiskelija": "01234561", "arvosana": 3, "kommentti": "miniprojekti rocks" })
ohtu.anna_palaute({ "opiskelija": "01234111", "arvosana": 1 })

ohtu.yhteenveto()