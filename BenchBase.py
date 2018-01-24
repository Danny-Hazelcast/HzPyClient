import Bench
import hazelcast
import sys


class BenchBase(Bench.Bench):

    def __init__(self):
        self.client = None  # type: hazelcast.HazelcastClient
        self.running = True
        self.name = None
        self.keyDomain = sys.maxint
        self.ignore = None


    def init(self):
        exceptions = self.ignore.split(":")


    def stop(self):
        self.running = False

    def isRunning(self):
        return self.running

    def setClient(self, client):
        self.client = client

    def postPhase(self):
        return

