from __future__ import division
from math import pow, sqrt
from fractions import gcd


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer / gcd(numer, denom)
        self.denom = denom / gcd(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational((self.numer * other.denom + other.numer * self.denom), (self.denom * other.denom))

    def __sub__(self, other):
        return Rational((self.numer * other.denom - other.numer * self.denom), (self.denom * other.denom))

    def __mul__(self, other):
        return Rational((self.numer * other.numer), (self.denom * other.denom))

    def __truediv__(self, other):
        return Rational((self.numer * other.denom), (other.numer * self.denom))

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power < 0:
            return Rational(pow(self.denom, abs(power)), pow(self.numer, abs(power)))
        else:
            return Rational(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        return pow(base, self.numer / self.denom)
