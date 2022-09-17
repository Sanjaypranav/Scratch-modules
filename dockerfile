FROM python:3.9.1-slim-buster
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
ADD . /app/
RUN python setup.py install