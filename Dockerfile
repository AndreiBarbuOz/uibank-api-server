# Pull a pre-built alpine docker image with nginx and python3 installed
FROM tiangolo/uwsgi-nginx-flask:python3.7

# Copy the app contents to the image
COPY ./app /app

