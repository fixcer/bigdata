import scrapy
import time
import sys, io


from play_store.items import PlayStoreApp
class AppSpider(scrapy.Spider):
    name = 'apps';
    start_urls = ['https://play.google.com/store/apps/']
    base_url='https://play.google.com'


    def parse(self, response):
        categories = response.xpath('//li[@class="KZnDLd"]/a[@class="r2Osbf"]')
        count=0
        for category in categories:
            count+=1
            if((count<11) and (count>12) ):
                continue
            else:
                
                yield response.follow(category,callback=self.parse_category)
    def parse_category(self, response):
        urls = response.xpath('//div[@class="xwY9Zc"]/a/@href').extract()
        for url in urls:
            yield response.follow(url,callback=self.parse_link)

    def parse_link(self, response):
        urls = response.xpath('//div[@class="b8cIId ReQCgd Q9MA7b"]/a/@href').extract()
        for url in urls:
            yield response.follow(url, callback=self.parse_app)

    def parse_app(self, response):
        print(response.request.url)
        item=PlayStoreApp()
        item['title']=response.xpath('//h1[@class="AHFaub"]/span/text()').extract()
        item['size']=response.css('.hAyfc:nth-child(2) .htlgb::text').extract()
        item['installs'] = response.css('.hAyfc:nth-child(3) .htlgb::text').extract()
        item['reviews'] = response.css('.hzfjkd + span::text').extract()
        item['rating'] = response.css('.BHMmbe::text').extract()
        item['price'] = response.css('.IfEcue::text').extract()
        item['category'] = response.css('.UAO9ie+ .UAO9ie .R8zArc::text').extract()
        item['contentRating'] = response.css('.hAyfc:nth-child(6) .htlgb div:nth-child(1)::text').extract()
        item['lastUpdate'] = response.css('.hAyfc:nth-child(1) .htlgb::text').extract()
        item['currentVersion'] = response.css('.hAyfc:nth-child(4) .htlgb::text').extract()
        item['androidVersion'] = response.css('.hAyfc:nth-child(5) .htlgb::text').extract()
        yield item
