FROM bencouture/keybase
LABEL maintainer "bencouture (https://keybase.io/bencouture")

COPY * /home/keybase/

USER root
RUN apt-get update; apt-get install -y python3 python3-pip; \
	pip3 install -r requirements.txt
USER keybase

EXPOSE 4433

ENTRYPOINT keybase oneshot; python3 ~/keybase.py;
