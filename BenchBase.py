import Bench
import hazelcast
import sys
from pydoc import locate


class BenchBase(Bench.Bench):

    def __init__(self):
        self.client = None  # type: hazelcast.HazelcastClient
        self.running = True
        self.name = None
        self.keyDomain = sys.maxint
        self.ignore = None

    def init(self):
        names = self.ignore.split(":")

        exceptions = []
        for name in names:
            exceptions.append(locate(name))
        self.ignore = exceptions

    def stop(self):
        self.running = False

    def isRunning(self):
        return self.running

    def setClient(self, client):
        self.client = client

    def postPhase(self):
        return

    def ignore(self, exception):
        for ignored in self.ignore:
            if isinstance(exception, ignored):
                return True
        return False


