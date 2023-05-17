FROM jupyter/datascience-notebook:python-3.9.2

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /src
COPY . /src

LABEL mainteiner="Daniele D'Avino daniele.davino@live.it"
LABEL version="1.0"
LABEL description="Generalistic version"