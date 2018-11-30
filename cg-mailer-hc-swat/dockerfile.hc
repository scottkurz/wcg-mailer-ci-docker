FROM cgmailer:latest

COPY --chown=was:was jvm.hc.props /work/config/jvm.hc.props

# HealthCenter output
RUN mkdir /work/hc

RUN work/applyConfig.sh /work/config/jvm.hc.props
