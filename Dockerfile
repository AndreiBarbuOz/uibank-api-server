FROM python:3.8-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 80
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"

ENTRYPOINT ["python3"]

CMD ["./app/main.py"]