class Sovelluslogiikka:
    def __init__(self):
        self._arvo = 0
        self._previous_state = None

    def plus(self, arvo):
        self._previous_state = self._arvo
        self._arvo += arvo

    def miinus(self, arvo):
        self._previous_state = self._arvo
        self._arvo -= arvo

    def nollaa(self):
        self._previous_state = self._arvo
        self._arvo = 0

    def arvo(self):
        return self._arvo

    def get_current_state(self):
        return self._arvo

    def set_current_state(self, tila):
        self._arvo = tila

    def get_previous_state(self):
        return self._previous_state

    def has_previous_state(self):
        return self._previous_state