FROM python:3.11-alpine
RUN apk add --no-cache parallel
RUN apk add --no-cache jq
COPY process_anf.py .
COPY process_anf.sh .
VOLUME /input
VOLUME /output
ENTRYPOINT ["/process_anf.sh"]
