FROM python:3.6

WORKDIR /usr/src/carnival

ADD requirements-to-freeze.txt /usr/src/carnival

RUN pip install -r requirements-to-freeze.txt

ADD . /usr/src/carnival

