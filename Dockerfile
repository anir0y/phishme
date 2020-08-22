FROM python:3


RUN apt-get update -y

RUN apt-get install python3-pip -y

RUN apt-get install php7.0 -y

RUN apt-get install unzip -y

WORKDIR /root

RUN git clone https://github.com/anir0y/phishme.git

WORKDIR /root/phishme/base/Server/

RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip

RUN unzip ngrok-stable-linux-amd64.zip

RUN rm -rf ngrok-stable-linux-amd64.zip

WORKDIR /root/phishme

RUN pip3 install -r requirements.txt

RUN chmod +x phishme.py

RUN ln -s /root/phishme/phishme.py /bin/phishme


ENTRYPOINT ["/root/phishme/phishme.py"]

#CMD ["--help"]