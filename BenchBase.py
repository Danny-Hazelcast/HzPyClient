import Bench
import hazelcast


class BenchBase(Bench.Bench):

    def __init__(self):
        self.client = None  # type: hazelcast.HazelcastClient
        self.running = True
        self.name = None

    def stop(self):
        self.running = False

    def isRunning(self):
        return self.running

    def setClient(self, client):
        self.client = client

    def postPhase(self):
        return

