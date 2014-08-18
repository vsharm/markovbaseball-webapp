import json
from markov_calculator import markovCalculate

states =["0____","0_1__","0__2_","0___3","0_12_","0_1_3","0__23","0_123",
         "1____","1_1__","1__2_","1___3","1_12_","1_1_3","1__23","1_123",
         "2____","2_1__","2__2_","2___3","2_12_","2_1_3","2__23","2_123",]

stateDescriptions =["Empty, 0 Out","1b, 0 Out","2b, 0 Out","3b, 0 Out","1b 2b, 0 Out","1b 3b, 0 Out","2b 3b 0 Out","Loaded, 0 Out",
                    "Empty, 1 Out","1b, 1 Out","2b, 1 Out","3b, 1 Out","1b 2b, 1 Out","1b 3b, 1 Out","2b 3b, 1 Out","Loaded, 1 Out",
                    "Empty, 2 Out","1b, 2 Out","2b, 2 Out","3b, 2 Out","1b 2b, 2 Out","1b 3b, 2 Out","2b 3b, 2 Out","Loaded, 2 Out",]

def parseJsonTotals(data):
	totals = { "hits":0, "doubles":0, "triples":0, "hr":0, "sb":0, "cs":0, "hbp":0, "pa":0, "bb":0, }	
	for team in league:
		for player in team["players"]:
			for stats in player:
				if stats != 'name' and stats != 'team' and stats != 'url' and stats != 'year':
					totals[stats] += player[stats]
	totals["singles"] = totals["hits"] - totals["doubles"] - totals["triples"] - totals["hr"]
	totals.pop("hits", None)
	return totals

def perGameMarkovRuns(totals):
        return round(runsPerInning(totals)["0____"]*9,2)

def runsPerInning(totals):
	resultMatrix = markovCalculate(totals["singles"], totals["doubles"], totals["triples"], 
				       totals["hr"], totals["bb"], totals["hbp"], totals["pa"] )
        markovDict = {}
        count = 0
        for i in resultMatrix.getA1()[:len(resultMatrix.getA1())-1]:
            markovDict[states[count]] = round(i,2)
            count=count+1
        return markovDict

def markovStateRuns(totals):
	markovDict = runsPerInning(totals)
	returnDict = []
	for i in range(0,len(states)):
		returnDict.append( {"state":states[i], "ex_runs":markovDict[states[i]],"stateDescription":stateDescriptions[i]} )
	return returnDict
def bunting(totals):

	resultMatrix = markovCalculate(totals["singles"], totals["doubles"], totals["triples"], 
	                               totals["hr"], totals["bb"], totals["hbp"], totals["pa"] )
	
	output = []
	
	matrixArray = resultMatrix.getA1()	
	
	for i in [1, 2, 4, 5, 9, 10, 12, 13]:
		offset = 0
		if i == 4 or i == 12:
			offset = 10+i
		else:
			offset = i+9
		
		decision = ""
		if matrixArray[i] < resultMatrix.getA1()[offset]:
			decision = True
		else:
			decision = False
		results = {"pre_state":states[i], "post_state":states[offset], "decision":decision, 
                           "pre_expected_runs":round(matrixArray[i],2), "post_expected_runs":round(matrixArray[offset],2), 
			   "pre_description":stateDescriptions[i], "post_description":stateDescriptions[offset]}
		#print states[i]," ER Pre: ", round(matrixArray[i],2), " ", states[offset], " ER Post: ", round(matrixArray[offset],2) , " ", decision
		output.append(results)
	return output

def steals(totals):
	resultMatrix = markovCalculate(totals["singles"], totals["doubles"], totals["triples"], 
								   totals["hr"], totals["bb"], totals["hbp"], totals["pa"] )
	matrixArray = resultMatrix.getA1()
        
        if float(totals["sb"]+totals["cs"]) > 0:
	    sbSuccessPercent = float(totals["sb"])/float(totals["sb"] + totals["cs"])
        sbSuccessPercent = 0
	#print "SB Success Rate: ", sbSuccessPercent
	output = []
	for i in [1,2,4,5,9,10,12,13,17,18,20,21]:
			ERSteal = 0


			if i == 1 or i == 2:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + matrixArray[8]*(1-sbSuccessPercent)
			elif i == 4:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + matrixArray[9]*(1-sbSuccessPercent)
			elif i == 5:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + matrixArray[11]*(1-sbSuccessPercent)
			elif i == 9 or i == 10:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + matrixArray[16]*(1-sbSuccessPercent)
			elif i == 12:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + matrixArray[17]*(1-sbSuccessPercent)
			elif i == 13:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + matrixArray[19]*(1-sbSuccessPercent)
			elif i == 17 or i == 18 or i == 20 or i == 21:
				ERSteal = matrixArray[i+1]*sbSuccessPercent + 0

			decision = ""
			if matrixArray[i] > ERSteal:
				decision = False
			else:
				decision = True
			#print states[i], " ER Pre: ", round(matrixArray[i],2), " ", states[i+1], " ER Post: ", round(ERSteal,2) , " ", decision
			results = {"pre_state": states[i], "post_state": states[i+1], "decision": decision, 
                                   "pre_expected_runs": round(matrixArray[i],2), "post_expected_runs":round(ERSteal,2),
				   "pre_description":stateDescriptions[i], "post_description":stateDescriptions[i+1]}
			output.append(results)
	return output
