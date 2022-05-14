FROM fedora:36
FROM python:3

RUN apt-get update && apt-get -y install \
    build-essential libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev wget unzip curl
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
RUN unzip ngrok-stable-linux-amd64.zip
RUN mv ./ngrok /usr/bin/ngrok
RUN git clone https://github.com/vihaan-s1ngla/mcserverlauncher-ngrok.git
RUN apt -y install python3-pip
WORKDIR "mcserverlauncher-ngrok"
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
