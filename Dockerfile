# pull official base image
FROM python:3.8.3-alpine


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies

RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev


# set work directory
RUN mkdir /app
WORKDIR /app
    
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt


# copy project
COPY . /app/
