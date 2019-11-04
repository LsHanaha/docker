FROM python:3.7

RUN apt-get update && \
    apt-get upgrade -y

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
COPY . /app

# ENV FLASK_ENV="docker"
EXPOSE 5000
