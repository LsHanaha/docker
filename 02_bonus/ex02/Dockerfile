FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_RUN_HOST 0.0.0.0
ENV FLASK_APP app.py

RUN apk add --no-cache gcc musl-dev linux-headers
COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/app.py app/

WORKDIR /code/app

CMD ["flask", "run"]
