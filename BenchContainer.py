from ReplyMsg import ReplyMsg
from pydoc import locate
from multiprocessing.dummy import Pool as ThreadPool
import time
import jsonpickle

class BenchContainer(object):

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
        for o in self.tasks:
            o.init()

    def setField(self, field, val):
        for o in self.tasks:
            setattr(o, field, val)

    def run(self, seconds, connection, replyQ):
        pool = ThreadPool(len(self.tasks))
        for t in self.tasks:
            pool.apply_async(marker, (self.driverId, t, self.taskId, seconds, connection, replyQ))


def marker(driverId, task, taskId, seconds, connection, replyQ):

    msg = ReplyMsg(Id=driverId, benchId=taskId, msg='end')

    end = time.time() + seconds
    while time.time() < end:
        try:
            task.timeStep()
        except Exception as e:
            print e
            msg.error = True
            msg.msg = e.message
            break

    msg = jsonpickle.pickler.encode(msg)
    print("MQ msg out = " + msg)
    connection.send(body=msg, destination=replyQ)
