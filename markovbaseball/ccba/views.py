from django.http import HttpResponse
from django.shortcuts import render
import json
import os
from analysis import *

# Create your views here.
def indexPage(request):
    print "index"
    data = json.load(open(os.path.expanduser("~/markov_baseball/sortedCCBA.json")))
    return render(request, 'index.html', {"teams": data.keys()})

def index(request,urlpath = "/"):
    print "teamRouter", urlpath
    URLPartition = urlpath.split("/")
    urllen = len(URLPartition)

    data = json.load(open(os.path.expanduser("~/markov_baseball/sortedCCBA.json")))


    print "URLPartiton ", URLPartition, " URLLen " ,urllen
    if(urlpath == "/"):
        returnRender = indexPage(request)
    elif(urllen == 2):
        returnRender = teamPage(request,data,teamName = URLPartition[1])
    elif(urllen == 3):
        returnRender = teamYear(request,data,teamName =  URLPartition[1], year = URLPartition[2])
    return returnRender

def teamPage(request,data, teamName):

    for k, v in data[teamName].items():
	if k == "year":
	    del data[teamName][k] 

    for year in data[teamName]:
   	data = generateTeamYearStatistics(data,teamName,year)

    returnDict = {
	"team": teamName,
        "stats":[],
        "m_steals_runs":None,
        "m_bunting_runs":None,
        "m_total_runs_game":None,
        "m_state_runs": None,
        "stat_totals":None,
        "years":[],
        "teams":[]
    } 

    for year in data[teamName]:
        returnDict["years"].append(year.encode('latin-1'))
	data[teamName][year]["stats"] = calculateRateStatistics(totaledStats = {
	    "ab": totalStatisticGivenKey("ab",data[teamName][year]["players"]),
            "pa": totalStatisticGivenKey("pa",data[teamName][year]["players"]),
	    "bb": totalStatisticGivenKey("bb",data[teamName][year]["players"]),
            "hits": totalStatisticGivenKey("hits",data[teamName][year]["players"]),
            "doubles": totalStatisticGivenKey("doubles",data[teamName][year]["players"]),
            "triples": totalStatisticGivenKey("triples",data[teamName][year]["players"]),
	    "hr": totalStatisticGivenKey("hr",data[teamName][year]["players"]),
	    "sb": totalStatisticGivenKey("sb",data[teamName][year]["players"]),
	    "cs": totalStatisticGivenKey("cs",data[teamName][year]["players"]),
	    "hbp": totalStatisticGivenKey("hbp",data[teamName][year]["players"]),
	})
	returnDict["stats"].append(data[teamName][year]["stats"])
    
    data[teamName]["stat_totals"] = calculateRateStatistics(totaledStats = {
            "ab": totalStatisticGivenKey("ab",returnDict["stats"]),
            "pa": totalStatisticGivenKey("pa",returnDict["stats"]),
            "bb": totalStatisticGivenKey("bb",returnDict["stats"]),
            "hits": totalStatisticGivenKey("hits",returnDict["stats"]),
            "doubles": totalStatisticGivenKey("doubles",returnDict["stats"]),
            "triples": totalStatisticGivenKey("triples",returnDict["stats"]),
            "hr": totalStatisticGivenKey("hr",returnDict["stats"]),
            "sb": totalStatisticGivenKey("sb",returnDict["stats"]),
            "cs": totalStatisticGivenKey("cs",returnDict["stats"]),
            "hbp": totalStatisticGivenKey("hbp",returnDict["stats"]),
        })
    for teamKey in data:
      returnDict["teams"].append(teamKey)


    returnDict["stat_totals"] = data[teamName]["stat_totals"]
    
    returnDict["m_steals_runs"] = steals(data[teamName]["stat_totals"])
    returnDict["m_bunting_runs"] = bunting(data[teamName]["stat_totals"])
    returnDict["m_total_runs_game"] = perGameMarkovRuns(data[teamName]["stat_totals"])
    returnDict["m_state_runs"] = markovStateRuns(data[teamName]["stat_totals"])

    return render(request, 'team.html',returnDict)
    #return HttpResponse(json.dumps(returnDict), content_type="application/json")

def teamYear(request,data, teamName, year):
    print "teamYear"
    teamKeys=[]
    for teamKey in data:
    	teamKeys.append(teamKey)

    team = generateTeamYearStatistics(data,teamName,year)    
    data = team[teamName][year]
    data["years"] = [data["year"].encode('latin-1')]
    del data["year"]

    data["stat_totals"] = calculateRateStatistics(totaledStats = {
        "ab": totalStatisticGivenKey("ab",data["players"]),
        "pa": totalStatisticGivenKey("pa",data["players"]),
        "bb": totalStatisticGivenKey("bb",data["players"]),
        "hits": totalStatisticGivenKey("hits",data["players"]),
        "doubles": totalStatisticGivenKey("doubles",data["players"]),
        "triples": totalStatisticGivenKey("triples",data["players"]),
        "hr": totalStatisticGivenKey("hr",data["players"]),
        "sb": totalStatisticGivenKey("sb",data["players"]),
        "cs": totalStatisticGivenKey("cs",data["players"]),
        "hbp": totalStatisticGivenKey("hbp",data["players"]),
    })

    count=0
    stylingList = [1,2,3,4,5] 
    for player in range(0,len(data["players"])):
	count+=1
    	data["players"][player]["m_steals_runs"] = steals(data["players"][player])
    	data["players"][player]["m_bunting_runs"] = bunting(data["players"][player])
    	data["players"][player]["m_total_runs_game"] = perGameMarkovRuns(data["players"][player])
    	data["players"][player]["m_state_runs"] = markovStateRuns(data["players"][player])
	data["players"][player]["id"] = player
        data["players"][player]["styleID"] = stylingList[count%5]
    data["team"] = teamName
    data["teams"]=teamKeys
    data["players_json"] = json.dumps(data["players"])
    #return HttpResponse(json.dumps(data), content_type="application/json")
    return render(request, 'year_team.html',data)

def generateTeamYearStatistics(data,teamName,year):
    print teamName,year
    arrayOfPlayerDictionaries = data[teamName][year]["players"]
    teamPlayerStats = totalTeamStats(arrayOfPlayerDictionaries)
    teamPlayerStats = calculateRateStatistics(totaledStats = teamPlayerStats)
    
    #calculate rate stats for each player
    for playerIndex in range(0,len(arrayOfPlayerDictionaries)):
        arrayOfPlayerDictionaries[playerIndex] = calculateRateStatistics(arrayOfPlayerDictionaries[playerIndex])
    
    #calculate each markov runs for the team data        
    data[teamName][year]["m_total_runs_game"] = perGameMarkovRuns(teamPlayerStats)
    data[teamName][year]["m_state_runs"] = markovStateRuns(teamPlayerStats)
    data[teamName][year]["m_bunting_runs"] = bunting(teamPlayerStats)
    data[teamName][year]["m_steals_runs"] = steals(teamPlayerStats)

    return data


def totalTeamStats(arrayOfPlayerDictionaries):
    totalDict = {}
    if arrayOfPlayerDictionaries != 0:
        for statTypeKey in arrayOfPlayerDictionaries[0]:
            #dont want to total stats that are strings
            if not(  isinstance(arrayOfPlayerDictionaries[0][statTypeKey], str) 
              or isinstance(arrayOfPlayerDictionaries[0][statTypeKey], unicode) ):
                    totalDict[statTypeKey] = totalStatisticGivenKey(statTypeKey,arrayOfPlayerDictionaries)
    return totalDict


def totalStatisticGivenKey(key,arrayOfStatDictionaries):
    total = 0
    for dictionary in arrayOfStatDictionaries:
       total += dictionary[key]
    return total

def calculateRateStatistics(totaledStats):
    hits = totaledStats["hits"]
    pa = totaledStats["pa"]
    walks = totaledStats["bb"]
    doubles = totaledStats["doubles"]
    triples = totaledStats["triples"]
    hr = totaledStats["hr"]
    sb = totaledStats["sb"]
    cs = totaledStats["cs"]
    hbp = totaledStats["hbp"]
    singles = hits - doubles - triples - hr
    ab = pa - walks
    
    #totaled Stats
    totaledStats["ab"] = ab
    totaledStats["singles"] = singles
    totaledStats["sb_success"] = round(float(sb)/float(cs+sb),2) if sb+cs else 0    
    totaledStats["avg"] = round(float(hits)/float(ab),3) if ab else 0
    totaledStats["obp"] = round(float(walks+hbp+hits)/float(pa),3) if pa else 0
    totaledStats["bb_percent"] = round(float(walks)/float(pa),2) if pa else 0
    totaledStats["slg"] = round(float(singles + 2*doubles + 3*triples + 4*hr)/float(ab),3) if ab else 0

    return totaledStats
