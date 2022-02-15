FROM python:3.10-alpine
MAINTAINER Aaron


ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
ENV PORT 8080
# must add this DB dependency when using postgres. It must be added before the pip install
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
# Delete temporary requirments tmp-build-deps(which is what we named it)
RUN apk del .tmp-build-deps


RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user