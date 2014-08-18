import json
f =  open("ccba.json")
allTeamsInHistory = json.load(f)

teams = {}
for teamInHistory in allTeamsInHistory:
	teams[teamInHistory["teamName"]] = {"year":None}

for teamInHistory in allTeamsInHistory:
	teams[teamInHistory["teamName"]][teamInHistory["year"]] = teamInHistory

with open("sortedCCBA.json", "w") as outfile:
    json.dump(teams, outfile)
