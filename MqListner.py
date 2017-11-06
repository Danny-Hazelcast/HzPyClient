from collections import namedtuple
import jsonpickle
import stomp


class MqListener(stomp.ConnectionListener):
    def __init__(self, controller):
        self.controller = controller

    def on_error(self, headers, message):
        print('error %s' % headers)
        print('error %s' % message)

    def on_message(self, headers, message):
        replyQ = headers['reply-to']
        print("MQ msg in = " + message)
        msg = jsonpickle.unpickler.decode(message)
        cmd = namedtuple("Cmd", msg.keys())(*msg.values())

        if cmd.cmd == 'StartEmbeddedObjectCmd':
            self.controller.bootClient(replyQ)

        elif cmd.cmd == 'LoadCmd':
            self.controller.loadBench(replyQ, cmd.taskId, cmd.className)

        elif cmd.cmd == 'ThreadCountCmd':
            self.controller.setThreadCount(replyQ, cmd.taskId, cmd.threadCount)

        elif cmd.cmd == 'SetFieldCmd':
            self.controller.setField(replyQ, cmd.taskId, cmd.field, cmd.value)

        elif cmd.cmd == 'SetBenchTypeCmd':
            self.controller.setBenchAttr(replyQ, cmd.taskId, cmd.type, cmd.intervalNanos, cmd.recordException, cmd.outFile)

        elif cmd.cmd == 'InitCmd':
            self.controller.initBench(replyQ, cmd.taskId)

        elif cmd.cmd == 'WarmupCmd':
            self.controller.warmupBench(replyQ, cmd.taskId, cmd.seconds)

        elif cmd.cmd == 'RunBenchCmd':
            self.controller.runBench(replyQ, cmd.taskId, cmd.seconds)

        elif cmd.cmd == 'PostPhaseCmd':
            self.controller.postPhase(replyQ, cmd.taskId)

        elif cmd.cmd == 'MetaDataCmd':
            self.controller.setMetaData(replyQ, cmd.taskId, cmd.metaData)

        elif cmd.cmd == 'RemoveBenchCmd':
            self.controller.removeBench(replyQ, cmd.taskId)

        elif cmd.cmd == 'StopBenchCmd':
            self.controller.stopBench(replyQ, cmd.taskId)

        else:
            raise NotImplementedError(message+" msg not implemented")

