
import hazelcast
import hazelcast.exception

import BenchMap
from random import randint


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        k = randint(0, int(self.keyDomain) - 1)
        try:
            val = self.map.get(k)
        except hazelcast.exception.HazelcastError as e:
            print e

        #if val is None:
        #    raise TypeError(" ")
