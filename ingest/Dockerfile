FROM alpine:3.18.5
RUN apk add --no-cache wget
COPY sources.txt .
ENTRYPOINT wget -x -nH --cut-dirs=1 -P /data -i sources.txt
