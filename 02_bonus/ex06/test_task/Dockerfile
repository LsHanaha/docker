FROM python:3.7

LABEL "author"="Trishin"

RUN apt-get update
RUN mkdir /test_task

COPY requirements.txt /test_task
WORKDIR /test_task
RUN pip install --no-cache-dir -r requirements.txt

COPY . /test_task
EXPOSE 8080

CMD [ "python3", "start.py" ]
