# Apache Spark Standalone Cluster on Docker

This project gives you an **Apache Spark** cluster in standalone mode with a **JupyterLab** interface built on top of **Docker**.
Learn Apache Spark through its **Python** (PySpark) API by running the Jupyter notebooks with examples on how to read, process and write data.

## Contents

- [Quick Start](#quick-start)
- [Tech](#tech)
- [Reference](#reference)

## <a name="quick-start"></a>Quick Start

### Cluster overview

| Application          | URL                                        |
| -------------------- | ------------------------------------------ |
| Hadoop               | [localhost:9870](http://localhost:9870/)   |
| MapReduce            | [localhost:8089](http://localhost:8089/)   |
| HUE                  | [localhost:8088](http://localhost:8088/)   |
| Mongo Cluster        | [localhost:21017](http://localhost:21017/) |
| Kafka Manager        | [localhost:9000](http://localhost:9000/)   |
| JupyterLab           | [localhost:8888](http://localhost:8888/)   |
| Spark Master         | [localhost:8080](http://localhost:8080/)   |

### Prerequisites

- Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

### Build from Docker Hub

1. Download the source code or clone the repository
2. Build the cluster

```bash
docker-compose up -d
```

3. Remove the cluster by typing

```bash
docker-compose down
```
## <a name="tech"></a>Tech

### Mongo Sharded Cluster 

##### WARNING (Windows & OS X) 

>The default Docker setup on Windows and OS X uses a VirtualBox VM to host the Docker daemon. 
>Unfortunately, the mechanism VirtualBox uses to share folders between the host system and 
>the Docker container is not compatible with the memory mapped files used by MongoDB 
>(see [vbox bug](https://www.virtualbox.org/ticket/819), [docs.mongodb.org](https://docs.mongodb.com/manual/administration/production->notes/#fsync-on-directories) 
>and related [jira.mongodb.org bug](https://jira.mongodb.org/browse/SERVER-8600)). 
>This means that it is not possible to run a MongoDB container with the data directory mapped to the host.
>
>&#8211; Docker Hub ([source here](https://github.com/docker-library/docs/blob/b78d49c9dffe5dd8b3ffd1db338c62b9e1fc3db8/mongo/content.md#where-to-store-data) 
>or [here](https://github.com/docker-library/mongo/issues/232#issuecomment-355423692))


## <a name="reference"></a>Reference

- [André Perez](https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker)
- [Big Data Europe - Hadoop Docker](https://github.com/big-data-europe/docker-hadoop)
- [Big Data Europe - Spark Docker](https://github.com/big-data-europe/docker-spark)
- [Minhhungit](https://github.com/minhhungit/mongodb-cluster-docker-compose)
