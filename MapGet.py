import BenchMap
from random import randint


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        k = randint(0, int(self.keyDomain)-1)
        val = self.map.get(k)

        #if val is None:
        #    raise TypeError(" ")
