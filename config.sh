#!/bin/bash

docker-compose exec configsvr01 sh -c "mongo < /scripts/init-configserver.js"
# sleep 5

docker-compose exec shard01-a sh -c "mongo < /scripts/init-shard01.js"
# sleep 5

docker-compose exec shard02-a sh -c "mongo < /scripts/init-shard02.js"
# sleep 5

docker-compose exec shard03-a sh -c "mongo < /scripts/init-shard03.js"
# sleep 5

docker-compose exec router01 sh -c "mongo < /scripts/init-router.js"
echo "\nDone!"

# docker-compose exec router01 mongo --port 27017
# sh.enableSharding("bigdata")
# db.adminCommand( { shardCollection: "bigdata.apps", key: { supplierId: "hashed" } } )
# exit
