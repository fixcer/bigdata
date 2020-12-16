# -*- coding: utf-8 -*-

from scrapy import signals
from pydispatch import dispatcher
from scrapy.exporters import JsonItemExporter
from datetime import date
from scrapy.utils.serialize import ScrapyJSONEncoder
from scrapy.utils.serialize import ScrapyJSONEncoder

from kafka  import KafkaClient
from kafka import KafkaProducer


class AppsPipeline(object):
    def process_item(self, item, spider):
        return item



class KafkaPipeline(object):

    def __init__(self, producer, topic):

        self.producer = producer
        self.topic = topic

        self.encoder = ScrapyJSONEncoder()

    def process_item(self, item, spider):
        self.producer.send_messages(self.topic, item)

    @classmethod
    def from_settings(cls, settings):
   
        k_hosts = settings.get('SCRAPY_KAFKA_HOSTS', ['kafka:9092'])
        topic = settings.get('SCRAPY_KAFKA_ITEM_PIPELINE_TOPIC', 'scrapy_kafka_item')
        kafka = KafkaClient(k_hosts)
        conn = KafkaProducer(kafka)
        return cls(conn, topic)
