'''
MQ msg in = {"cmd":"StartEmbeddedObjectCmd"}
MQ msg out = {"benchId": null, "error": false, "benchClazz": null, "threadId": null, "msg": "started on 192.168.1.103 81573 3.7.2", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","className":"hzcmd.map.Put","cmd":"LoadCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": "hzcmd.map.Put", "threadId": null, "msg": "load", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","threadCount":1,"cmd":"ThreadCountCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "put set 1 threads", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","type":"Metrics","intervalNanos":0,"recordException":true,"outFile":"HZ-put","cmd":"SetBenchTypeCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "set bench attributes", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","field":"keyDomain","value":"1000","cmd":"SetFieldCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "set keyDomain to 1000", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","cmd":"InitCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "init", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","seconds":1,"cmd":"WarmupCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "warming", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","seconds":0,"cmd":"RunBenchCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "running", "id": "PyClient2HZ"}

MQ msg in = {"taskId":".*","cmd":"StopBenchCmd"}
MQ msg out = {"benchId": ".*", "error": false, "benchClazz": null, "threadId": null, "msg": "stopping", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","cmd":"PostPhaseCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "post phase", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","metaData":"HZ M1C2 3.8-HzPyClient put hzcmd.map.Put 1 [driver\u003d.*, threads\u003d1, warmup\u003d1, duration\u003d0, bench\u003dMetrics, interval\u003d0, recordException\u003dtrue, keyDomain\u003d1000, valueSize\u003d101, name\u003dmapBak1]","cmd":"MetaDataCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "meta data", "id": "PyClient2HZ"}

MQ msg in = {"taskId":"put","cmd":"RemoveBenchCmd"}
MQ msg out = {"benchId": "put", "error": false, "benchClazz": null, "threadId": null, "msg": "remove bench", "id": "PyClient2HZ"}
'''


class ReplyMsg(object):
    def __init__(self, Id):
        self.id = Id
        self.benchId = None
        self.threadId = None
        self.benchClazz = None
        self.error = False
        self.msg = None

    def __init__(self, Id, benchId=None, threadId=None, benchClazz=None, error=False, msg=None):
        self.id = Id
        self.benchId = benchId
        self.threadId = threadId
        self.benchClazz = benchClazz
        self.error = error
        self.msg = msg

    def setErrorMsg(self, msg):
        self.error = True
        self.msg = msg
        with open('exception.txt', 'a') as f:
            f.write(msg)
