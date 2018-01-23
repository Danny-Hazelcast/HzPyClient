import BenchMap
from random import randint


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        self.map.get(0)
#       self.map.get(randint(0, self.keyDomain))
