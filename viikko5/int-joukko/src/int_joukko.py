KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:

    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = self.set_kapasiteetti(kapasiteetti)
        self.kasvatuskoko = self.set_kasvatuskoko(kasvatuskoko)
        self.ljono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def set_kapasiteetti(self, kapasiteetti):
        if kapasiteetti is None:
            return KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            return kapasiteetti
    
    def set_kasvatuskoko(self, kasvatuskoko):
        if kasvatuskoko is None:
            return OLETUSKASVATUS
        elif not isinstance(self.kapasiteetti, int) or self.kapasiteetti < 0:
            raise Exception("kapasiteetti2")
        else:
            return kasvatuskoko

    def kuuluu(self, alkio):

        for i in range(0, self.alkioiden_lkm):
            if alkio == self.ljono[i]:
                return True
        return False

    def _lisaa_ensimmainen_alkio_listaan(self, alkio):
        if self.alkioiden_lkm == 0:
            self.ljono[0] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass
    
    def kasvata_listan_kokoa(self):
        if self.alkioiden_lkm % len(self.ljono) == 0:
            taulukko_old = self.ljono
            self.kopioi_lista(self.ljono, taulukko_old)
            self.ljono = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
            self.kopioi_lista(taulukko_old, self.ljono)
            return True
        return False

    def lisaa(self, alkio):
        self._lisaa_ensimmainen_alkio_listaan(alkio)

        if not self.kuuluu(alkio):
            self.ljono[self.alkioiden_lkm] = alkio
            self.alkioiden_lkm = self.alkioiden_lkm + 1

        return self.kasvata_listan_kokoa()

    def _hae_alkio(self, alkio):
        for x in range(self.alkioiden_lkm):
            if alkio == self.ljono[x]:
                return True
        return False

    def _hae_alkion_indeksi(self, alkio):
        for x in range(self.alkioiden_lkm):
            if alkio == self.ljono[x]:
                return x

    def _poista_alkio_indeksista(self, indeksi):
        for y in range(indeksi, self.alkioiden_lkm - 1):
            self.ljono[y] = self.ljono[y + 1]
        self.alkioiden_lkm -= 1

    def poista(self, alkio):
        if self._hae_alkio(alkio):
            indeksi = self._hae_alkion_indeksi(alkio)
            self._poista_alkio_indeksista(indeksi)
            return True
        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = self._luo_lista(self.alkioiden_lkm)

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
