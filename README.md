# BigData

Learn Big Data through its **Python** (PySpark) API by running the Jupyter notebooks with examples on how to read, process and write data.

<img src="https://dytvr9ot2sszz.cloudfront.net/wp-content/uploads/2018/02/Kafka-Hadoop-Spark-Architecture-1024x666.png" style="width: 100%;" />
<img src="https://i.ibb.co/bR5YXxp/kafka-kibana.png" style="width: 120%;" />

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
./config.sh
```

3. Remove the cluster by typing

```bash
docker-compose down
```
## <a name="tech"></a>Tech

### Hadoop

<img src="https://images.prismic.io/clubhouse/81445563b0f9a0f7f1c09860c1bc8fc7980fa5d1_hadoop-data-nodes.png" style="width: 50%;" />


### Apache Spark Standalone Cluster

<img src="https://i.ibb.co/Pz4KsWZ/cluster-architecture.png" style="width: 100%;" />

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

##### Mongo Components

* Config Server (3 member replica set): `configsvr01`,`configsvr02`,`configsvr03`
* 3 Shards (each a 3 member `PSS` replica set):
	* `shard01-a`,`shard01-b`, `shard01-c`
	* `shard02-a`,`shard02-b`, `shard02-c`
	* `shard03-a`,`shard03-b`, `shard03-c`
* 2 Routers (mongos): `router01`, `router02`

<img src="https://raw.githubusercontent.com/minhhungit/mongodb-cluster-docker-compose/master/images/sharding-and-replica-sets.png" style="width: 100%;" />

## <a name="reference"></a>References

- [André Perez](https://github.com/cluster-apps-on-docker/spark-standalone-cluster-on-docker)
- [Big Data Europe - Hadoop Docker](https://github.com/big-data-europe/docker-hadoop)
- [Big Data Europe - Spark Docker](https://github.com/big-data-europe/docker-spark)
- [Minhhungit](https://github.com/minhhungit/mongodb-cluster-docker-compose)
