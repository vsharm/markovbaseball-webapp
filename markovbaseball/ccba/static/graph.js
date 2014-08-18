function graph(yearsList,graphData){
    		var graphlistsettings = {"avg":null,"obp":null,"slg":null,"sb_success":null,"bb_percent":null};
    	 		
		if(yearsList.length > 1){
    			for( type in graphlistsettings){
    			graphlistsettings[type] = {
    				labels : yearsList,
    				datasets : [
    					{
    					label: "My First dataset",
    					fillColor : "rgba(220,220,220,0.2)",
    					strokeColor : "rgba(220,220,220,1)",
    					pointColor : "rgba(220,220,220,1)",
    					pointStrokeColor : "#fff",
    					pointHighlightFill : "#fff",
    					pointHighlightStroke : "rgba(220,220,220,1)",
    					data : graphData[type]
    					},
    				]
    			};
    			}

    		}
    			var barGraphListSettings = {
        			labels:graphData["ex_runs_descriptions"],
        			datasets: [{
                				label: "My First dataset",
                				fillColor: "rgba(220,220,220,0.5)",
                				strokeColor: "rgba(220,220,220,0.8)",
                				highlightFill: "rgba(220,220,220,0.75)",
                				highlightStroke: "rgba(220,220,220,1)",
                				data: graphData["ex_runs"]
            			  }]
    			};
    		var twoColumnBarGraphSettings = {"m_bunting_runs":null,"m_steals_runs":null};
    		for(type in twoColumnBarGraphSettings){
    		   twoColumnBarGraphSettings[type] = {
                            labels : graphData[type+"_descriptions"],
                            datasets : [
                                    {
                                            label: "Pre",
                                            fillColor : "rgba(220,220,220,0.2)",
                                            strokeColor : "rgba(220,220,220,1)",
                                            pointColor : "rgba(220,220,220,1)",
                                            pointStrokeColor : "#fff",
                                            pointHighlightFill : "#fff",
                                            pointHighlightStroke : "rgba(220,220,220,1)",
                                            data : graphData[type+"_pre"]
                                    },
    				{
                                            label: "Post",
                                            fillColor : "rgba(220,220,220,0.2)",
                                            strokeColor : "rgba(220,220,220,1)",
                                            pointColor : "rgba(220,220,220,1)",
                                            pointStrokeColor : "#fff",
                                            pointHighlightFill : "#fff",
                                            pointHighlightStroke : "rgba(220,220,220,1)",
                                            data : graphData[type+"_post"]
                                    },
                            ]

                       };	
    		}
    	window.onload = function(){
    		var graphs = {"avg":null,"obp":null,"slg":null,"sb_success":null,"bb_percent":null};
    		var twoColumnBarGraph = {"m_bunting_runs":null, "m_steals_runs":null};
    		if(yearsList.length > 1){
			for(type in graphs){
    				graphs[type] = document.getElementById(type+"-graph").getContext("2d");
    				window.myLine = new Chart(graphs[type]).Line(graphlistsettings[type], {
    					responsive: true,
    					scaleShowGridLines : false,
    					scaleStepWidth:.01,
                                        scaleFontColor : "#dfdfdf"
    				});
    			}
		}
                var barGraph = document.getElementById("m_state_runs-graph").getContext("2d");
                            window.myLine = new Chart(barGraph).Bar(barGraphListSettings, {
                                    responsive: true,
                                    scaleShowGridLines : false,
                                    scaleStepWidth:.01,
                                    scaleFontColor : "#dfdfdf"
                            });
                    for(type in twoColumnBarGraph){
                            twoColumnBarGraph[type] = document.getElementById(type+"-graph").getContext("2d");
                            window.myLine = new Chart(twoColumnBarGraph[type]).Bar(twoColumnBarGraphSettings[type], {
                                    responsive: true,
                                    scaleShowGridLines : false,
                                    scaleStepWidth:.01,
                                    scaleFontColor : "#dfdfdf"
                            });
                    }
    	}
    }

function perPlayerGraphs(players,m_steals_runs_descriptions,m_bunting_runs_descriptions){
	var typeArray = ["m_steals_runs", "m_bunting_runs"];
	var typeDescriptions= {"m_steals_runs": m_steals_runs_descriptions, "m_bunting_runs":m_bunting_runs_descriptions};
	var graphSettingsArray = {"m_steals_runs":[],"m_bunting_runs":[]};




                        var barGraphListSettings = {
                                labels:graphData["ex_runs_descriptions"],
                                datasets: [{
                                                label: "My First dataset",
                                                fillColor: "rgba(220,220,220,0.5)",
                                                strokeColor: "rgba(220,220,220,0.8)",
                                                highlightFill: "rgba(220,220,220,0.75)",
                                                highlightStroke: "rgba(220,220,220,1)",
                                                data: graphData["ex_runs"]
                                  }]
                        };

                var twoColumnBarGraphSettings = {"m_bunting_runs":null,"m_steals_runs":null};
                for(type in twoColumnBarGraphSettings){
                   twoColumnBarGraphSettings[type] = {
                            labels : graphData[type+"_descriptions"],
                            datasets : [
                                    {
                                            label: "Pre",
                                            fillColor : "rgba(220,220,220,0.2)",
                                            strokeColor : "rgba(220,220,220,1)",
                                            pointColor : "rgba(220,220,220,1)",
                                            pointStrokeColor : "#fff",
                                            pointHighlightFill : "#fff",
                                            pointHighlightStroke : "rgba(220,220,220,1)",
                                            data : graphData[type+"_pre"]
                                    },
                                {
                                            label: "Post",
                                            fillColor : "rgba(220,220,220,0.2)",
                                            strokeColor : "rgba(220,220,220,1)",
                                            pointColor : "rgba(220,220,220,1)",
                                            pointStrokeColor : "#fff",
                                            pointHighlightFill : "#fff",
                                            pointHighlightStroke : "rgba(220,220,220,1)",
                                            data : graphData[type+"_post"]
                                    },
                            ]

                       };
                }

	for (type in typeArray){
		for(playerIndex in players){
			    var m_runs_obj = players[playerIndex][typeArray[type]];
			    var pre_data = [];
			    var post_data = [];
			    for(state in m_runs_obj){
				pre_data.push(m_runs_obj[state]["pre_expected_runs"]);
				post_data.push(m_runs_obj[state]["post_expected_runs"]);
			    }
	                    graphSettingsArray[typeArray[type]].push({
                            labels : typeDescriptions[typeArray[type]],
                            datasets : [
                                    {
                                            label: "Pre",
                                            fillColor : "rgba(220,220,220,0.2)",
                                            strokeColor : "rgba(220,220,220,1)",
                                            pointColor : "rgba(220,220,220,1)",
                                            pointStrokeColor : "#fff",
                                            pointHighlightFill : "#fff",
                                            pointHighlightStroke : "rgba(220,220,220,1)",
                                            data : pre_data
                                    },
                                    {
                                            label: "Post",
                                            fillColor : "rgba(220,220,220,0.2)",
                                            strokeColor : "rgba(220,220,220,1)",
                                            pointColor : "rgba(220,220,220,1)",
                                            pointStrokeColor : "#fff",
                                            pointHighlightFill : "#fff",
                                            pointHighlightStroke : "rgba(220,220,220,1)",
                                            data : post_data
                                    },
                            ]

                       	});
		}
	}
	var twoColumnBarGraph = {"m_bunting_runs":[], "m_steals_runs":[]};
	window.onload = function(){

		var twoColumnBarGraphTeam = {"m_bunting_runs":null, "m_steals_runs":null};
                var barGraph = document.getElementById("m_state_runs-graph").getContext("2d");
                            window.myLine = new Chart(barGraph).Bar(barGraphListSettings, {
                                    responsive: true,
                                    scaleShowGridLines : false,
                                    scaleStepWidth:.01,
                                    scaleFontColor : "#dfdfdf"
                            });
                    for(type in twoColumnBarGraph){
                            twoColumnBarGraphTeam[type] = document.getElementById(type+"-graph").getContext("2d");
                            window.myLine = new Chart(twoColumnBarGraphTeam[type]).Bar(twoColumnBarGraphSettings[type], {
                                    responsive: true,
                                    scaleShowGridLines : false,
                                    scaleStepWidth:.01,
                                    scaleFontColor : "#dfdfdf"
                            });
                    }
	


                   for(typeIndex in typeArray){
			    var type  = typeArray[typeIndex];
			    for(index in graphSettingsArray[type]){
                            twoColumnBarGraph[type].push(document.getElementById(type+"-graph-"+index).getContext("2d"));
                            window.myLine = new Chart(twoColumnBarGraph[type][index]).Bar(graphSettingsArray[type][index], {
                                    responsive: true,
                                    scaleShowGridLines : false,
                                    scaleStepWidth:.01,
				    animation:false,
                                    scaleFontColor : "#dfdfdf"
                            });

			    }
                  }
	}
}
