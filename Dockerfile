# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
# RUN pip3 install --force-reinstall --no-cache-dir pycairo==1.26.0
RUN pip install -r requirements.txt
COPY . /code/
