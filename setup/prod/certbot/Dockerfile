FROM debian:stable

RUN apt-get update \
  && apt-get install -y letsencrypt \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  && mkdir -p /etc/letsencrypt