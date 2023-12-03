from enum import Enum
from tkinter import ttk, constants, StringVar
from sovelluslogiikka import Sovelluslogiikka

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Summa:
    def __init__(self, io):
        self.io = io
        self.previous_state = None

    def suorita(self, syote):
        self.previous_state = self.io.get_current_state()
        self.io.plus(syote)


class Erotus:
    def __init__(self, io):
        self.io = io
        self.previous_state = None

    def suorita(self, syote):
        self.previous_state = self.io.get_current_state()
        self.io.miinus(syote)


class Nollaus:
    def __init__(self, io):
        self.io = io
        self.previous_state = None

    def suorita(self, arvo):
        self.previous_state = self.io.get_current_state()
        self.io.nollaa()

class Kumoa:
    def __init__(self, io):
        self.io = io

    def suorita(self, syote):
        if self.io.has_previous_state():
            self.io.set_current_state(self.io.get_previous_state())

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovellus = sovelluslogiikka
        self._root = root

        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus),
            Komento.EROTUS: Erotus(self._sovellus),
            Komento.NOLLAUS: Nollaus(self._sovellus),
            Komento.KUMOA: Kumoa(self._sovellus)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovellus.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.KUMOA)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)

    def _lue_syote(self):
        arvo = 0
        try:
            arvo = int(self._syote_kentta.get())
        except:
            pass
        return arvo

    def _suorita_komento(self, komento):
        komento_olio = self._komennot[komento]
        komento_olio.suorita(self._lue_syote())

        if komento == Komento.KUMOA:
            self._kumoa_painike["state"] = constants.DISABLED
        else:
            self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovellus.arvo())
