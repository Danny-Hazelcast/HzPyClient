import sys
import HzControler

brokerIP = sys.argv[1]
queueId = sys.argv[2]
Id = sys.argv[3]
clusterID = sys.argv[4]

controller = HzControler.HzControler(brokerIP, queueId, Id, clusterID, sys.argv[5:])
controller.start()
