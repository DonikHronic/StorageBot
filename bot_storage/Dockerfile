FROM python:3.9.14-slim-buster
ENV HOME=/home/app

RUN mkdir -p $HOME
WORKDIR $HOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . $HOME
RUN pip install -r requirements.txt