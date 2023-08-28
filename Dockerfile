FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
  xinetd \
  python3-pip \
  python3-dev \
  && rm -rf /var/lib/apt/lists/*

RUN useradd -M -d /ctf ctf

RUN mkdir /home/ctf
WORKDIR /home/ctf

RUN echo "Connection blocked" > /etc/banner_fail
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY ./src /home/ctf/

RUN chown -R ctf:ctf /home/ctf && chmod -R 770 /home/ctf

RUN chown -R root:ctf /home/ctf && \
  chmod -R 750 /home/ctf


ENTRYPOINT []
CMD ["/usr/sbin/xinetd", "-dontfork"]

EXPOSE 9999
