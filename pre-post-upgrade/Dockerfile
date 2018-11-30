FROM ibmcom/websphere-traditional:latest

# Create Mailer DB
COPY --chown=was:was CreateMailerTablesDerby.ddl /work/ddl/mailer.ddl
#COPY --chown=was:was CreateSmallerMailerTablesDerby.ddl /work/ddl/mailer.ddl
RUN [ "/opt/IBM/WebSphere/AppServer/java/8.0/bin/java", "-Dij.database=jdbc:derby:/work/mailerdb;create=true" , \
   "-Djava.ext.dirs=/opt/IBM/WebSphere/AppServer/derby/lib", "org.apache.derby.tools.ij", \
   "/work/ddl/mailer.ddl" \
    ]

# Copy app stuff
COPY --chown=was:was Mailer.xml /work/xjcl/

ADD --chown=was:was profileBackup.tar.gz /work

# not sure if updating a started server makes sense so let's not use the configure.sh script
RUN /opt/IBM/WebSphere/AppServer/profiles/AppSrv01/bin/WASPostUpgrade.sh /work/profileBackup -oldProfile AppSrv01 -profileName AppSrv01   -backupConfig false -clone true

# let the password get set to whatever... probably should be mounting a volume if a give one is desired.

