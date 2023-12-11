FROM alpine:3.18.5
RUN apk add --no-cache wget
COPY sources.txt .
VOLUME /data
ENTRYPOINT [\
    "wget",\
    "--no-verbose",\
    "--force-directories",\
    "--no-host-directories",\
    "--cut-dirs=1",\
    "--directory-prefix=/data",\
    "--input-file=sources.txt"]
