FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl git gettext-base
COPY generate_and_apply_certificates.sh .
COPY ca_config.txt .
RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"
RUN chmod +x kubectl && mv kubectl /usr/local/bin/
