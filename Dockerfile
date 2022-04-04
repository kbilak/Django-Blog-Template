FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /Django-Blog-Template

COPY Pipfile Pipfile.lock /Django-Blog-Template/
RUN pip install pipenv && pipenv install --system

COPY . /Django-Blog-Template/