import sys

SID="WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1"

PROJ_LOC = "/work/app/"


SWAT_EAR = 'swat.ear'
SWAT_LOC = PROJ_LOC + SWAT_EAR


print "Installing SWAT app"

AdminApp.install(SWAT_LOC, '[ -nopreCompileJSPs -distributeApp -nouseMetaDataFromBinary -nodeployejb -appname swat -createMBeansForResources -noreloadEnabled -nodeployws -validateinstall warn -noprocessEmbeddedConfig -filepermission .*\.dll=755#.*\.so=755#.*\.a=755#.*\.sl=755 -noallowDispatchRemoteInclude -noallowServiceRemoteInclude -asyncRequestDispatchType DISABLED -nouseAutoLink -noenableClientModule -clientMode isolated -novalidateSchema -MapModulesToServers [[ swat swat.war,WEB-INF/web.xml WebSphere:cell=DefaultCell01,node=DefaultNode01,server=server1 ]]]' ) 

print "SWAT app installed, saving..."
AdminConfig.save()
