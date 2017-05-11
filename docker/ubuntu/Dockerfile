FROM continuumio/miniconda3
MAINTAINER Lukasz Kuczynski <kuczynskilukasz@gmail.com>

RUN apt-get install unzip
RUN wget https://github.com/lukaszkuczynski/scout/archive/master.zip
RUN unzip master.zip
WORKDIR scout-master

RUN conda install --yes --file requirements.txt

ENTRYPOINT python web/web.py
EXPOSE 5000
