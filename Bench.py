

class Bench(object):
    def init(self):
        raise NotImplementedError("implement this method")

    def timeStep(self):
        raise NotImplementedError("implement this method")

    def postPhase(self):
        raise NotImplementedError("implement this method")

    def ignore(self, exception):
        raise NotImplementedError("implement this method")

    def stop(self):
        raise NotImplementedError("implement this method")

    def isRunning(self):
        raise NotImplementedError("implement this method")

    def setVendorObject(self, vendorObject):
        raise NotImplementedError("implement this method")

