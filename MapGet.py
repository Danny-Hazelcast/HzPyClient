from hazelcast.exception import TimeoutError, TargetDisconnectedError

import BenchMap
from random import randint


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        k = randint(0, int(self.keyDomain) - 1)
        val = self.map.get(k)

    # try:
    #except TimeoutError as e:
        #    return
        #except TargetDisconnectedError as e:
        #    return

        #if val is None:
        #    raise TypeError(" ")
