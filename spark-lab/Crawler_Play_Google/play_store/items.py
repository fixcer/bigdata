from scrapy.item import Item, Field


class PlayStoreApp(Item):
    size=Field()
    title=Field()
    installs=Field()
    reviews=Field()
    rating=Field()
    price=Field()
    category=Field()
    contentRating=Field()
    lastUpdate=Field()
    currentVersion=Field()
    androidVersion=Field()
