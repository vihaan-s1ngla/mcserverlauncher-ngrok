FROM ubuntu:20.04
FROM python:3

RUN apt-get update && apt-get -y install \
    build-essential libpcre3 libpcre3-dev zlib1g zlib1g-dev libssl-dev wget unzip
RUN wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
RUN unzip ngrok-stable-linux-amd64.zip
RUN mv ./ngrok /usr/bin/ngrok
RUN mkdir mcserverlauncher-ngrok && mcserverlauncher-ngrok