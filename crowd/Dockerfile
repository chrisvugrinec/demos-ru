#FROM centos:8
FROM arm64v8/centos:latest

RUN yum update  
    dnf upgrade -y && \
    dnf module -y install nodejs:14 && \
    dnf install -y python3 python3-devel git-all && \
    dnf group install -y "Development Tools" && \
    pip3 install --upgrade pip setuptools && \
    pip3 install aws-sam-cli awscli
