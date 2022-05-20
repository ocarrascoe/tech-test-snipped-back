# Pulling an official base image
FROM python:3.9-alpine

# Declaring maintainer
MAINTAINER Omar Carrasco

# Setting environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Europe/Madrid

# Installing psycopg2 dependencies
RUN apk add git
RUN apk add --update --no-cache postgresql-client
RUN apk add --no-cache curl jq python3 py3-pip
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libpq libc-dev linux-headers postgresql-dev postgresql-libs
RUN pip3 install --upgrade pip
RUN pip3 install -U --force-reinstall pip
RUN apk --update --upgrade add gcc g++ cargo musl-dev jpeg-dev python3-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install Pillow
RUN pip3 install --no-use-pep517 --upgrade Cython
# RUN pip3 install --no-use-pep517 --upgrade numpy
# RUN pip3 install --no-use-pep517 --upgrade pandas
RUN apk add tzdata

# Installing dependencies
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setting Up directory structure
RUN mkdir /app
WORKDIR /app
COPY ./src /app

# Adding and run as non-root user
RUN adduser -D user
USER user
