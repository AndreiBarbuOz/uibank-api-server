FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y python3.7 python3-pip && \
    python3.7 -m pip install pipenv

RUN mkdir /app
WORKDIR /app

COPY Pipfile /app
COPY Pipfile.lock /app
RUN pipenv install --python 3.7 --system

ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP=/app/hello.py
COPY hello.py /app

CMD ["flask","run", "--host", "0.0.0.0"]
