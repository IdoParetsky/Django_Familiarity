FROM python:3.6
RUN apt-get -y update
RUN apt-get -y install git nano
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN pip install mysqlclient  uwsgi
COPY . .
EXPOSE 8000