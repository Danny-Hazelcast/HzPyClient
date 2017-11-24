import BenchMap


class BenchMapPut(BenchMap.BenchMap):

    def timeStep(self):
        self.map.put(1, 2)
