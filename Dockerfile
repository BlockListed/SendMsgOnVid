FROM ubuntu:latest

COPY . /opt/SendMsgOnVid

RUN apt update

RUN apt upgrade -y

RUN apt install -y python3-pip

RUN pip3 install discord.py requests