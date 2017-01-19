FROM python:3.6

RUN groupadd -r carnival && useradd -r -g carnival carnival

WORKDIR /home/carnival/.carnival

ADD requirements-to-freeze.txt /home/carnival/.carnival

RUN pip install -r requirements-to-freeze.txt

RUN chown -R carnival.carnival /home/carnival

RUN apt-get autoremove -y

USER carnival
