# Apache Spark Standalone Cluster on Docker

This project gives you an **Apache Spark** cluster in standalone mode with a **JupyterLab** interface built on top of **Docker**.
Learn Apache Spark through its **Python** (PySpark) API by running the Jupyter notebooks with examples on how to read, process and write data.

## Contents

- [Quick Start](#quick-start)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [Contributors](#contributors)

## <a name="quick-start"></a>Quick Start

### Cluster overview

| Application            | URL                                      | Description                                                |
| ---------------------- | ---------------------------------------- | ---------------------------------------------------------- |
| Hadoop                 | [localhost:9870](http://localhost:9870/) |                                                            |
| YARN                   | [localhost:8089](http://localhost:8089/) |                                                            |
| HUE                    | [localhost:8088](http://localhost:8088/) |                                                            |
| JupyterLab             | [localhost:8888](http://localhost:8888/) | Cluster interface with built-in Jupyter notebooks          |
| Apache Spark Master    | [localhost:8080](http://localhost:8080/) | Spark Master node                                          |

### Prerequisites

 - Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
 
 ### Build from Docker Hub

1. Download the source code or clone the repository;
2. Build the cluster;

```bash
docker-compose up -d
```
3. Stop the cluster by typing
```bash
docker-compose down
```
