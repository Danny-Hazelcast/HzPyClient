import BenchBase


class BenchMap(BenchBase.BenchBase):

    def __init__(self):
        self.map = None

    def init(self):
        self.map = self.client.get_map(self.name)
