import BenchBase


class BenchMap(BenchBase.BenchBase):

    def __init__(self):
        super(BenchMap, self).__init__()
        self.map = None

    def init(self):
        self.map = self.client.get_map(self.name).blocking()
