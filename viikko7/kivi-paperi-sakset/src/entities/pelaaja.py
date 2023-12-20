class Pelaaja:
    def __init__(self):
        self._siirto = str(None)

    def hae_siirto(self):
        return self._siirto

    def aseta_siirto(self, siirto):
        self._siirto = siirto

class EasyAI(Pelaaja):
    def __init__(self):
        super().__init__()
        self._siirto = 0

    def aseta_siirto(self):
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"

    def hae_siirto(self):
        if self._siirto == 0:
            return "k"
        elif self._siirto == 1:
            return "p"
        else:
            return "s"
        
class HardAI(Pelaaja):
    def __init__(self):
        super().__init__()
        self._siirrot = []

    def aseta_siirto(self):
        siirto = self._anna_siirto()
        self._lisaa_uusi_siirto(siirto)
        return siirto

    def hae_siirto(self):
        if not self._siirrot:
            return super().hae_siirto()
        return self._siirrot[-1]

    def _lisaa_uusi_siirto(self, siirto):
        if len(self._siirrot) == 10:
            self._siirrot.pop(0)
        self._siirrot.append(siirto)

    def _anna_siirto(self):
        if len(self._siirrot) <= 1:
            return "k"

        viimeisin_siirto = self._siirrot[-1]

        k = 0
        p = 0
        s = 0

        for i in range(len(self._siirrot) - 1):
            if viimeisin_siirto == self._siirrot[i]:
                seuraava = self._siirrot[i + 1]

                if seuraava == "k":
                    k = k + 1
                elif seuraava == "p":
                    p = p + 1
                else:
                    s = s + 1

        if k > p or k > s:
            return "p"
        elif p > k or p > s:
            return "s"
        else:
            return "k"
