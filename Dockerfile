# syntax=docker/dockerfile:1
FROM python:3.9.1-slim

RUN apt-get update

WORKDIR /code
COPY .. /code

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

