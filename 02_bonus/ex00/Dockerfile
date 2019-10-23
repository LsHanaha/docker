FROM ubuntu

LABEL author="Lshanaha"

RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install python3 python3-pip -y
RUN mkdir -p /opt/app

WORKDIR /opt/app

EXPOSE 5000 80

COPY app/requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY app /opt/app

CMD ["python3", "app.py"]
