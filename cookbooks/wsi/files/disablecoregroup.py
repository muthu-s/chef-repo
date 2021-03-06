import os;
import sys;
import traceback;

#####################################################################
## Disable Core group service at JVM level
#####################################################################

def modifyHAManager(clusterName, isEnabled, isActivateEnabled):
            print "Cluster Name = " + clusterName + "\n"
            clusterID = AdminConfig.getid("/ServerCluster:" + clusterName + "/")
            serverList=AdminConfig.list('ClusterMember', clusterID)
            servers=serverList.split("\n")

            for serverID in servers:
                    serverName=AdminConfig.showAttribute(serverID, 'memberName')
                    print "ServerName = " + serverName + "\n"
                    server=AdminConfig.getid("/Server:" +serverName + "/")
                    process = AdminConfig.list("HAManagerService",server)
                    AdminConfig.modify(process, [ ["enable", isEnabled], ["activateEnabled", isActivateEnabled] ])
                    AdminConfig.save()
                    print "Core Group service disabled for : " +serverName + "\n"


#####################################################################
## Main
#####################################################################
if len(sys.argv) != 3:
        print "This script requires clusterName, isEnabled, isActivateEnabled"
        sys.exit(1)
else:
        clusterName = sys.argv[0]
        isEnabled = sys.argv[1]
        isActivateEnabled = sys.argv[2]
        modifyHAManager(clusterName, isEnabled, isActivateEnabled)
