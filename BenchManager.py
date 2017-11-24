from BenchContainer import BenchContainer

class BenchManager(object):

    def __init__(self, driverID, client):
        self.tasks = {}
        self.driverID = driverID
        self.client = client

    def loadBench(self, id, className):
        self.tasks[id] = BenchContainer(self.driverID, self.client, id, className)

    def setThreadCount(self, id, count):
        self.tasks[id].createInstances(count)

    def init(self):
        for t in self.tasks.values():
            t.init()

    def setField(self, id, field, value):
        self.tasks[id].setField(field, value)

    def run(self, id, seconds, connection, replyQ):
        self.tasks[id].run(seconds, connection, replyQ)