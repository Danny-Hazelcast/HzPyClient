
import hazelcast
import hazelcast.exception

import BenchMap
from random import randint


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        k = randint(0, int(self.keyDomain) - 1)
        try:
            val = self.map.get(k)
        except Exception as e:
            print e
            pass


        #if val is None:
        #    raise TypeError(" ")
