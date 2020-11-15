import sys
import json
from pyspark.sql import SparkSession, DataFrame
from pyspark import SparkContext, SparkConf


if __name__ == "__main__":

    # create Spark context with Spark configuration
    spark = SparkSession.builder.master("spark://spark-master:7077").appName("Tutorial").getOrCreate()

    df = spark.read.format("json").load("hdfs://namenode/user/root/input/data10.json", multiLine="true")

    df = df.groupby('androidVersion').count().sort('count', ascending=False)

    df.rdd.saveAsTextFile("hdfs://namenode/user/root/output")
