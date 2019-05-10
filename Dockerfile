FROM tiangolo/uwsgi-nginx-flask:python3.7

MAINTAINER Tim Showers "tim.showers@govhawk.com"

ENV LISTEN_PORT 5080
EXPOSE 5080

COPY ./app /app

RUN pip3 install -r /app/requirements.txt
