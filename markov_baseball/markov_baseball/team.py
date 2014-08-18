from scrapy.item import Item, Field

class ParentTeam(Item):
	teamName = Field()
	players  = Field()
	year 	 = Field()


