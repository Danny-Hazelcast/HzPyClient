import BenchMap
from random import randint


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        k = randint(0, self.keyDomain)
        val = self.map.get(k)
