import sys

SID="WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1"

#print "Importing apps from CAR"
#print AdminTask.importApplicationsFromWasprofile('[-archive /work/config/profile.car -targetNodeName DefaultNode01 -targetServerName server1 -sourceServerName server1]')

print "Importing profile from CAR"
print AdminTask.importWasprofile('[-archive /work/config/profile.car -deleteExistingServers true]')
AdminConfig.save()
