FROM apache/kafka:3.8.0

WORKDIR /home/appuser

RUN wget https://downloads.apache.org/kafka/3.8.0/kafka_2.13-3.8.0.tgz
RUN tar -xvzf kafka_2.13-3.8.0.tgz

ENV PATH="$PATH:/home/appuser/kafka_2.13-3.8.0/bin"