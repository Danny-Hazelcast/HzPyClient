import time
import os
import socket
from ReplyMsg import ReplyMsg
from MqListner import *


class Controler(object):

    def __init__(self):
        self.conn = None
        self.brokerIP = None
        self.queueId = None
        self.Id = None
        self.version = None

    def start(self):
        self.conn = stomp.Connection([(self.brokerIP, 61613)])
        self.conn.set_listener('', MqListener(self))
        self.conn.start()
        self.conn.connect('', '', wait=True)
        self.conn.subscribe(destination='/queue/'+self.queueId, id=1, ack='auto')

        while True:
            time.sleep(1)

    def init(self):
        raise NotImplementedError("implement this method")

    def bootClient(self, replyQ):
        msg = ReplyMsg(Id=self.Id)
        try:
            self.init()
            msg.msg='started on '+socket.gethostbyname(socket.gethostname())+" "+str(os.getpid())+" "+self.version
        except Exception as e:
            msg.error = True
            msg.msg = e.message +" version "+ self.version

        self.sendReply(replyQ=replyQ, msg=msg)

    def loadBench(self, replyQ, taskId, className):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='load')
        self.sendReply(replyQ=replyQ, msg=msg)

    def setThreadCount(self, replyQ, taskId, threadCount):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set'+str(threadCount)+" threads")
        self.sendReply(replyQ=replyQ, msg=msg)

    def setField(self, replyQ, taskId, field, value):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set '+field+' to '+value)
        self.sendReply(replyQ=replyQ, msg=msg)

    def setBenchAttr(self, replyQ, taskId, type, intervalNanos, recordException, outFile):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='set bench attributes')
        self.sendReply(replyQ=replyQ, msg=msg)

    def initBench(self, replyQ, taskId):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='init')
        self.sendReply(replyQ=replyQ, msg=msg)

    def warmupBench(self, replyQ, taskId, seconds):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='warming')
        self.sendReply(replyQ=replyQ, msg=msg)

    def runBench(self, replyQ, taskId, seconds):
        msg = ReplyMsg(Id=self.Id, benchId=taskId, msg='running')
        self.sendReply(replyQ=replyQ, msg=msg)

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
