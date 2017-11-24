import os
import socket
import time
from ReplyMsg import ReplyMsg
from MqListner import *
from TaskMaster import *


class Controller(object):

    def __init__(self):
        self.conn = None
        self.brokerIP = None
        self.queueId = None
        self.Id = None
        self.version = None
        self.tasks = None

    def start(self):
        self.conn = stomp.Connection([(self.brokerIP, 61613)])
        self.conn.set_listener('', MqListener(self))
        self.conn.start()
        self.conn.connect('', '', wait=True)
        self.conn.subscribe(destination='/queue/'+self.queueId, id=1, ack='auto')

        while True:
            time.sleep(1)

    def init(self):
        raise NotImplementedError("Controller init implement this method")

    def getClient(self):
        raise NotImplementedError("Controller getClient implement this method")

    def bootClient(self, replyQ):
        msg = ReplyMsg(Id=self.Id, msg='started on '+socket.gethostbyname(socket.gethostname())+" "+str(os.getpid())+" "+self.version )
        try:
            self.init()
            self.tasks = TaskMaster(self.Id, self.getClient())
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def load(self, replyQ, taskId, className):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='load')
        try:
            self.tasks.load(taskId, className)
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def setThreadCount(self, replyQ, taskId, threadCount):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set'+str(threadCount)+" threads")
        try:
            self.tasks.setThreadCount(taskId, threadCount)
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def setField(self, replyQ, taskId, field, value):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set '+field+' to '+value)
        try:
            self.tasks.setField(taskId, field, value)
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def setBenchAttr(self, replyQ, taskId, type, intervalNanos, recordException, outFile):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='')
        self.sendReply(replyQ=replyQ, msg=msg)

    def initTasks(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='init')
        try:
            self.tasks.init()
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def warmup(self, replyQ, taskId, seconds):
        self.tasks.run(taskId, seconds, self.conn, replyQ)

    def run(self, replyQ, taskId, seconds):
        self.tasks.run(taskId, seconds, self.conn, replyQ)

    def postPhase(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='post phase')
        try:
            self.tasks.postPhase(taskId)
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def setMetaData(self, replyQ, taskId, metaData):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='')
        self.sendReply(replyQ=replyQ, msg=msg)

    def remove(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='remove bench')
        try:
            self.tasks.remove(taskId)
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def stop(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='stopping')
        try:
            self.tasks.stop(taskId)
        except Exception as e:
            msg.setErrorMsg(e.message)
        self.sendReply(replyQ=replyQ, msg=msg)

    def sendReply(self, replyQ, msg):
        msg = jsonpickle.pickler.encode(msg)
        print("MQ msg out = " + msg)
        self.conn.send(body=msg, destination=replyQ)
