FROM debian:latest
LABEL author="lshanaha"
ENV TS3SERVER_LICENSE=accept 

WORKDIR /home/teamspeak

RUN apt-get -y update && \
    apt-get -y upgrade
RUN apt-get install -y wget bzip2 &&\
    wget https://files.teamspeak-services.com/releases/server/3.9.1/teamspeak3-server_linux_amd64-3.9.1.tar.bz2 && \
    tar -xf *.tar.bz2

EXPOSE 9987/udp 10011 30033

WORKDIR teamspeak3-server_linux_amd64/

ENTRYPOINT ["sh", "ts3server_minimal_runscript.sh"]

# docker build -t ts_server .
# docker run -p 10011:10011 -p 30033:30033 -p 9987:9987/udp  -it ts_server:latest
