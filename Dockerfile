FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

WORKDIR /app

RUN pip install -r flask-serv-req.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

