FROM ubuntu:18.04

LABEL maintainer="Toan <toannv.soict@gmail.com>"

ENV ENABLE_INIT_DAEMON true
ENV INIT_DAEMON_BASE_URI http://identifier/init-daemon
ENV INIT_DAEMON_STEP spark_master_init

ENV SPARK_VERSION=3.0.0
ENV HADOOP_VERSION=3.2

COPY wait-for-step.sh /
COPY execute-step.sh /
COPY finish-step.sh /

RUN apt-get update && \
	apt-get install -y software-properties-common && \
	rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:openjdk-r/ppa && \
	add-apt-repository ppa:deadsnakes/ppa && \
	apt-get update && \
	apt-get install -y \
	curl \
	wget \
	bash \
	openjdk-8-jre \
	python3.7 \
	python3-pip && \
	apt-get clean

RUN ln -s /lib64/ld-linux-x86-64.so.2 /lib/ld-linux-x86-64.so.2 \
	&& chmod +x *.sh \
	&& wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
	&& tar -xvzf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
	&& mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark \
	&& rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
	&& cd /

# Give permission to execute scripts
RUN chmod +x /wait-for-step.sh && chmod +x /execute-step.sh && chmod +x /finish-step.sh

# Set python3 as default
ENV PYSPARK_PYTHON python3

# Fix the value of PYTHONHASHSEED
# Note: this is needed when you use Python 3.3 or greater
ENV PYTHONHASHSEED 1
