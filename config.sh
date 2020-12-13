#!/bin/bash

docker-compose exec configsvr01 sh -c "mongo < /scripts/init-configserver.js"

docker-compose exec shard01-a sh -c "mongo < /scripts/init-shard01.js"
docker-compose exec shard02-a sh -c "mongo < /scripts/init-shard02.js"
docker-compose exec shard03-a sh -c "mongo < /scripts/init-shard03.js"

docker-compose exec router01 sh -c "mongo < /scripts/init-router.js"

# docker-compose exec router01 mongo --port 27017
# sh.enableSharding("bigdata")
# db.adminCommand( { shardCollection: "bigdata.apps", key: { supplierId: "hashed" } } )
# exit
