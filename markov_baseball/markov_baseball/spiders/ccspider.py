from scrapy.spider import Spider
from scrapy.selector import Selector

from markov_baseball.item import BaseballItem
from markov_baseball.team import ParentTeam

class CCBASpider(Spider):
    name = "ccba"
    allowed_domains = ["cccbca.com"]
    years = ["2012-13", "2011-12", "2013-14"]
    teams = ["contracosta", "laney", "losmedanos", "marin", "mendocino", "napa", "solano", "yuba"]
    start_urls = []
    for year in years:
        for team in teams:
            start_urls.append(
                "http://www.cccbca.com/sports/bsb/"+ year +"/bayvalley/teams/" + team + "?view=lineup"
            )

    def extractDashedField(response, data):
        if data == '- ':
            return 0
        else:
            return int(data)


    def parse(self, response):
        sel = Selector(response)
        teamName = str(sel.xpath("//*[@id='mainbody']/div[2]/h2/text()").extract()[0])
        players = {}

        # general xpath query from this page
        # //*[@id='mainbody']/div[2]/div[3]/ (2 = hitting table 
        # 3 = extended table)div[2]/table/(player)tr[2]/(doubles)td[10]
        sites = sel.xpath("//*[@id='mainbody']/div[2]/div[3]/div[2]/table/tr")
        for i in range(1,len(sites)-2):
            item = BaseballItem()

            item["year"]    = response.url.rsplit('/', 4)[1]
            item["url"]     = response.url
            item["name"]    = str(sites[i].xpath("td/a/text()").extract()[0])[1:]
            item["team"]    = teamName
            item["hits"]    = self.extractDashedField((sites[i].xpath("td[9]/text()").extract()[0]))
            item["doubles"] = self.extractDashedField((sites[i].xpath("td[10]/text()").extract()[0]))
            item["triples"] = self.extractDashedField((sites[i].xpath("td[11]/text()").extract()[0]))
            item["sb"]      = self.extractDashedField((sites[i].xpath("td[16]/text()").extract()[0]))
            item["cs"]      = self.extractDashedField((sites[i].xpath("td[17]/text()").extract()[0]))
            item["hr"]      = self.extractDashedField((sites[i].xpath("td[12]/text()").extract()[0]))
            item["bb"]      = self.extractDashedField((sites[i].xpath("td[14]/text()").extract()[0]))
            players[item["name"]] = item
        

        sites = sel.xpath("//*[@id='mainbody']/div[2]/div[3]/div[3]/table/tr")
        for i in range(1,len(sites)-2):
            name = str(sites[i].xpath("td/a/text()").extract()[0])[1:]
            players[name]["pa"]  = self.extractDashedField((sites[i].xpath("td[16]/text()").extract()[0]))
            players[name]["hbp"] = self.extractDashedField((sites[i].xpath("td[7]/text()").extract()[0]))
        
        playerArray = []
        for name in players:
            playerArray.append(players[name])


        team = ParentTeam()
        team["teamName"] = teamName
        team["year"]     = response.url.rsplit('/', 4)[1]
        team["players"]  = playerArray
        return team

