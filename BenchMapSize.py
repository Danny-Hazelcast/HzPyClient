import BenchMap


class BenchMapSize(BenchMap.BenchMap):

    def __init__(self):
        super(BenchMapSize, self).__init__()
        self.size = 0

    def timeStep(self):
        if self.map.size() != int(self.size):
            raise Exception(str(self.map.size())+" != "+self.size)
        self.stop()
