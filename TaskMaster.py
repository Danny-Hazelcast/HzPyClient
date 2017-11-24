import re
from Task import Task


class TaskMaster(object):

    def __init__(self, driverID, client):
        self.tasks = {}
        self.driverID = driverID
        self.client = client

    def load(self, id, className):
        self.tasks[id] = Task(self.driverID, self.client, id, className)

    def setThreadCount(self, id, count):
        self.tasks[id].createInstances(count)

    def init(self):
        for t in self.tasks.values():
            t.init()

    def setField(self, id, field, value):
        self.tasks[id].setField(field, value)

    def run(self, id, seconds, connection, replyQ):
        self.tasks[id].run(seconds, connection, replyQ)

    def postPhase(self, id):
        self.tasks[id].postPhase()

    def stop(self, id):
        for t in self.tasks.values():
            if re.match(id, t.taskId) is not None:
                t.stop()

    def remove(self, id):
        self.tasks.pop(id)
