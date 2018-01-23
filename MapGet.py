import BenchMap


class MapGet(BenchMap.BenchMap):

    def timeStep(self):
        self.map.get(  self.keyDomain)
