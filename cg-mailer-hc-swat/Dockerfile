FROM ibmcom/websphere-traditional:latest

# Create Mailer DB
COPY --chown=was:was CreateMailerTablesDerby.ddl /work/ddl/mailer.ddl
#COPY --chown=was:was CreateSmallerMailerTablesDerby.ddl /work/ddl/mailer.ddl
RUN [ "/opt/IBM/WebSphere/AppServer/java/8.0/bin/java", "-Dij.database=jdbc:derby:/work/mailerdb;create=true" , \
   "-Djava.ext.dirs=/opt/IBM/WebSphere/AppServer/derby/lib", "org.apache.derby.tools.ij", \
   "/work/ddl/mailer.ddl" \
    ]

# Copy app stuff
COPY --chown=was:was MailerSample.ear /work/app/
COPY --chown=was:was SimpleCIEar.ear /work/app/
COPY --chown=was:was Mailer.xml /work/xjcl/

# Copy to a different name so it doesn't get run with every invocation to configure.sh
COPY --chown=was:was was-config.props /work/config/config.props

#
# Do it all
#

#COPY --chown=was:was scheduler-simple-ci-mailer.py /work/config/

# 1. Just configure scheduler
COPY --chown=was:was scheduler.py /work/config/
RUN /work/configure.sh /work/config/scheduler.py

# 2. security
COPY --chown=was:was security.py /work/config/
RUN /work/configure.sh /work/config/security.py

# 3. installApps
COPY --chown=was:was installApps.py /work/config/
RUN /work/configure.sh /work/config/installApps.py

# 4. mailer DS
COPY --chown=was:was mailerDS.py /work/config/
RUN /work/configure.sh /work/config/mailerDS.py

RUN work/applyConfig.sh /work/config/config.props

# 5. HealthCenter and JVM -X args
COPY --chown=was:was jvm.hc.props /work/config/jvm.hc.props
#--- output dir
RUN mkdir /work/hc
RUN work/applyConfig.sh /work/config/jvm.hc.props

# 6. install SWAT - most recently-changed part of the image
COPY --chown=was:was installSwat.py /work/config/
COPY --chown=was:was swat.ear /work/app/
RUN /work/configure.sh /work/config/installSwat.py

# 7. 
COPY --chown=was:was shrinkMailerDSPoolSize.py /work/config/
RUN /work/configure.sh /work/config/shrinkMailerDSPoolSize.py

