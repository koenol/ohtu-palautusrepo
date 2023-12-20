from entities.pelaaja import *
from entities.tuomari import Tuomari

class KPS:
    def __init__(self, Pelaaja1, Pelaaja2):
        self.pelaaja1 = Pelaaja1
        self.pelaaja2 = Pelaaja2
        self.tuomari = Tuomari()

    def kaksinpeli():
        return KPS(Pelaaja(), Pelaaja())

    def tekoaly_helppo():
        return KPS(Pelaaja(), EasyAI())
    
    def tekoaly_vaikea():
        return KPS(Pelaaja(), HardAI())

    def pelaa(self):
        if isinstance(self.pelaaja2, EasyAI):
            self.pelaaja2.aseta_siirto()
        if isinstance(self.pelaaja2, HardAI):
            self.pelaaja2.aseta_siirto()
        siirto1 = self.pelaaja1.hae_siirto()
        siirto2 = self.pelaaja2.hae_siirto()
        self.tuomari.kirjaa_siirto(siirto1, siirto2)
        self.tuomari.hae_pelitulos()