FROM debian:latest
LABEL author="lshanaha"
ENV TS3SERVER_LICENSE=accept 

WORKDIR /home/teamspeak

EXPOSE 9987/udp 10011 30033

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y wget bzip2 &&\
    wget http://dl.4players.de/ts/releases/3.0.13.8/teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2 && \
    tar -xf *.tar.bz2

WORKDIR teamspeak3-server_linux_amd64

ENTRYPOINT sh ts3server_minimal_runscript.sh
