from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import *
from pyspark.sql.types import *
from textblob import TextBlob

if __name__ == "__main__":

    # create Spark context with Spark configuration
    spark = SparkSession.builder \
        .master("spark://spark-master:7077") \
        .appName("Sentiment") \
        .getOrCreate()

    df = spark.read.format("json").load(
        "hdfs://namenode/user/root/input/data10.json", multiLine="true")

    df = df.na.drop().dropDuplicates()
    df = df.filter(size(df['comments']) >= 30)

    comments = df.select('comments').collect()
    schema = StructType([
        StructField('comment', StringType(), False),
        StructField('sentiment', IntegerType(), False),
    ])
    data = []

    for comment in comments:
        for item in comment[0]:
            try:
                sentiment = TextBlob(item).polarity

                if sentiment > 0:
                    data.append((item, 1))
                elif sentiment < 0:
                    data.append((item, -1))
                else:
                    data.append((item, 0))
            except:
                # item chua cac ki tu dac biet => None
                pass

    df = spark.createDataFrame(data, schema)

    df.write.csv("out.csv")
