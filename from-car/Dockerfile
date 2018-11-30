FROM ibmcom/websphere-traditional:latest

# Create Mailer DB
COPY --chown=was:was CreateMailerTablesDerby.ddl /work/ddl/mailer.ddl
#COPY --chown=was:was CreateSmallerMailerTablesDerby.ddl /work/ddl/mailer.ddl
RUN [ "/opt/IBM/WebSphere/AppServer/java/8.0/bin/java", "-Dij.database=jdbc:derby:/work/mailerdb;create=true" , \
   "-Djava.ext.dirs=/opt/IBM/WebSphere/AppServer/derby/lib", "org.apache.derby.tools.ij", \
   "/work/ddl/mailer.ddl" \
    ]

# Copy app stuff
COPY --chown=was:was importCar.py /work/config
COPY --chown=was:was profile.car /work/config
COPY --chown=was:was Mailer.xml /work/xjcl/

RUN /work/configure.sh 

