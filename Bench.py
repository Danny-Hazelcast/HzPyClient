

class Bench(object):

    def init(self):
        raise NotImplementedError("init implement this method")

    def timeStep(self):
        raise NotImplementedError("timeStep implement this method")

    def postPhase(self):
        raise NotImplementedError("postPhase implement this method")

    def ignore(self, exception):
        raise NotImplementedError("ignore implement this method")

    def stop(self):
        raise NotImplementedError("stop implement this method")

    def isRunning(self):
        raise NotImplementedError("isRunning implement this method")

    def setClient(self, client):
        raise NotImplementedError("setClient implement this method")

