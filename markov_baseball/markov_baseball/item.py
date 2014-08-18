from scrapy.item import Item, Field

class BaseballItem(Item):
    name    = Field()
    year    = Field()
    url     = Field()
    hits    = Field()
    doubles = Field()
    triples = Field()
    team    = Field()
    sb  	= Field()
    cs  	= Field()
    bb      = Field()
    hr      = Field()
    pa      = Field()
    hbp     = Field()

