FROM python:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/static
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app/
RUN pip install -r requirements.txt
ADD . /usr/src/app/
