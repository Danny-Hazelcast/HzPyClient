import sys
import HzControler

brokerIP = sys.argv[1]
queueId = sys.argv[2]
Id = sys.argv[3]
clusterID = sys.argv[4]

print("brokerIP = " + brokerIP)
print("queueId = " + queueId)
print("Id = " + Id)
print("clusterID = " + clusterID)

controller = HzControler.HzControler(brokerIP, queueId, Id, clusterID, sys.argv[5:])
controller.start()
