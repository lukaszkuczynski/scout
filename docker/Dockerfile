FROM luk/rpi-miniconda
MAINTAINER Lukasz Kuczynski <kuczynskilukasz@gmail.com>


RUN apt-get install unzip
RUN wget https://github.com/lukaszkuczynski/scout/archive/master.zip
RUN unzip master.zip
WORKDIR scout-master

RUN conda install pip
RUN pip install -r pip_requirements.txt
RUN conda install --yes --file conda_requirements.txt


EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["web/web.py"]

RUN python -m nltk.downloader stopwords 
RUN python -m nltk.downloader punkt
