import Controler
import hazelcast
import logging


class HzControler(Controler.Controler):

    def __init__(self, brokerIP, queueId, Id, clusterID, ips=[]):
        self.client = None
        self.brokerIP = brokerIP
        self.queueId = queueId
        self.Id = Id
        self.clusterID = clusterID
        self.ips = ips
        self.version = hazelcast.__version__

        logging.basicConfig()
        logging.getLogger().setLevel(logging.INFO)

    def init(self):

        config = hazelcast.ClientConfig()
        for ip in self.ips:
            config.network_config.addresses.append(ip+':5701')
        config.group_config.name = self.clusterID
        config.group_config.password = self.clusterID

        self.client = hazelcast.HazelcastClient(config)

    def getClient(self):
        return self.client
