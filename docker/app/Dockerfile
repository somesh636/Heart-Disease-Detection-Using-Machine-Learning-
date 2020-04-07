FROM ubuntu:bionic

RUN apt-get update -y
RUN apt-get install -y python3-pip python-dev

COPY ./app/ /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP main.py

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "80"]



