FROM python:3.8

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
		libkrb5-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN pip install --no-cache-dir -U pip setuptools wheel && \
    pip install --no-cache-dir poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY . ./

EXPOSE 8000
