FROM ubuntu:bionic
COPY apt.conf /etc/apt/apt.conf
ENV http_proxy "http://proxy.com:8080"
ENV https_proxy "http://proxy.com:8080"
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y net-tools
RUN apt-get install -y iperf3
RUN apt-get install -y iproute2
RUN apt-get install -y net-tools
RUN apt-get install -y python
RUN apt-get install -y wget
RUN apt-get install -y iputils-ping
RUN apt-get install -y netperf
WORKDIR /home
ENTRYPOINT ["bash"]