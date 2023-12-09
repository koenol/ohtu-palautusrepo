from matchers import *

class PinoRakentaja:
    def __init__(self, matcher: Matcher = All()):
        self.matcher = matcher

    def build(self) -> Matcher:
        return self.matcher

    def playsIn(self, team):
        return PinoRakentaja(And(self.matcher, PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        return PinoRakentaja(And(self.matcher, HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        return PinoRakentaja(And(self.matcher, HasFewerThan(value, attr)))

    def oneOf(self, *matchers:Matcher):
        return PinoRakentaja(Or(*matchers))
