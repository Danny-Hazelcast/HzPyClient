from ReplyMsg import ReplyMsg
from pydoc import locate
from multiprocessing.dummy import Pool as ThreadPool
import time
import jsonpickle
import sys
import traceback


class Task(object):

    def __init__(self, driverId, client, taskId, className):
        self.driverId = driverId
        self.client = client
        self.taskId = taskId
        self.className = className
        self.benchClazz = locate(className)
        self.tasks = []

    def createInstances(self, count):
        for i in range(0, count):
            self.tasks.append(self.benchClazz())
        for i in range(0, count):
            self.tasks[i].setClient(self.client)

    def init(self):
        for t in self.tasks:
            t.init()

    def setField(self, field, val):
        for t in self.tasks:
            setattr(t, field, val)

    def run(self, seconds, connection, replyQ):
        pool = ThreadPool(len(self.tasks))
        for t in self.tasks:
            pool.apply_async(marker, (self.driverId, t, self.taskId, seconds, connection, replyQ))

    def postPhase(self):
        for t in self.tasks:
            t.postPhase()

    def stop(self):
        for t in self.tasks:
            t.stop()


def marker(driverId, task, taskId, seconds, connection, replyQ):

    msg = ReplyMsg(Id=driverId, benchId=taskId, msg='end')

    if seconds == 0:
        seconds = sys.maxint

    end = time.time() + seconds
    while time.time() < end and task.isRunning():
        try:
            task.timeStep()
        except Exception as e:
            if not task.ignore(e):
                msg.setErrorMsg(e.message + " " + traceback.format_exc())
                break

    msg = jsonpickle.pickler.encode(msg)
    print("MQ msg out = " + msg)
    connection.send(body=msg, destination=replyQ)
