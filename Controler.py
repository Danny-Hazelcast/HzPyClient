import os
import socket
import time
from ReplyMsg import ReplyMsg
from MqListner import *
from BenchManager import *


class Controler(object):

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
        raise NotImplementedError("Controler init implement this method")

    def getClient(self):
        raise NotImplementedError("Controler getClient implement this method")

    def bootClient(self, replyQ):
        msg = ReplyMsg(Id=self.Id, msg='started on '+socket.gethostbyname(socket.gethostname())+" "+str(os.getpid())+" "+self.version )
        try:
            self.init()
            self.tasks = BenchManager(self.Id, self.getClient())
        except Exception as e:
            msg.error = True
            msg.msg = e.message
        self.sendReply(replyQ=replyQ, msg=msg)

    def loadBench(self, replyQ, taskId, className):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='load')
        try:
            self.tasks.loadBench(taskId, className)
        except Exception as e:
            msg.error = True
            msg.msg = e.message
        self.sendReply(replyQ=replyQ, msg=msg)

    def setThreadCount(self, replyQ, taskId, threadCount):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set'+str(threadCount)+" threads")
        try:
            self.tasks.setThreadCount(taskId, threadCount)
        except Exception as e:
            msg.error = True
            msg.msg = e.message
        self.sendReply(replyQ=replyQ, msg=msg)

    def setField(self, replyQ, taskId, field, value):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set '+field+' to '+value)
        try:
            self.tasks.setField(taskId, field, value)
        except Exception as e:
            msg.error = True
            msg.msg = e.message
        self.sendReply(replyQ=replyQ, msg=msg)

    def setBenchAttr(self, replyQ, taskId, type, intervalNanos, recordException, outFile):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set bench attributes')
        self.sendReply(replyQ=replyQ, msg=msg)

    def initBench(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='init')
        try:
            self.tasks.init()
        except Exception as e:
            msg.error = True
            msg.msg = e.message

        self.sendReply(replyQ=replyQ, msg=msg)

    def warmupBench(self, replyQ, taskId, seconds):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='warming')
        self.sendReply(replyQ=replyQ, msg=msg)

    def runBench(self, replyQ, taskId, seconds):
        self.tasks.run(taskId, seconds, self.conn, replyQ)

    def postPhase(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='post phase')
        self.sendReply(replyQ=replyQ, msg=msg)

    def setMetaData(self, replyQ, taskId, metaData):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='meta data')
        self.sendReply(replyQ=replyQ, msg=msg)

    def removeBench(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='remove bench')
        self.sendReply(replyQ=replyQ, msg=msg)

    def stopBench(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='stopping')
        self.sendReply(replyQ=replyQ, msg=msg)

    def sendReply(self, replyQ, msg):
        msg = jsonpickle.pickler.encode(msg)
        print("MQ msg out = " + msg)
        self.conn.send(body=msg, destination=replyQ)
