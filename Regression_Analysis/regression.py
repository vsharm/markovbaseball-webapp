import numpy
from scipy import stats
from numpy import linalg
import pylab
import csv
import prettyplotlib as ppl
import mpld3
import matplotlib.pyplot as plt
from mpld3 import plugins


states =["0____","0_1__","0__2_","0___3","0_12_","0_1_3","0__23","0_123",
         "1____","1_1__","1__2_","1___3","1_12_","1_1_3","1__23","1_123",
         "2____","2_1__","2__2_","2___3","2_12_","2_1_3","2__23","2_123",]

stateDescriptions =["Empty, 0 Out","1b, 0 Out","2b, 0 Out","3b, 0 Out","1b 2b, 0 Out","1b 3b, 0 Out","2b 3b 0 Out","Loaded, 0 Out",
                    "Empty, 1 Out","1b, 1 Out","2b, 1 Out","3b, 1 Out","1b 2b, 1 Out","1b 3b, 1 Out","2b 3b, 1 Out","Loaded, 1 Out",
                    "Empty, 2 Out","1b, 2 Out","2b, 2 Out","3b, 2 Out","1b 2b, 2 Out","1b 3b, 2 Out","2b 3b, 2 Out","Loaded, 2 Out",]

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

def markovCalculate(singles, doubles, triples, hr, walks, hbp, plateAppearences):
   pSingle = singles/float(plateAppearences) if singles else 0
   pDouble = doubles/float(plateAppearences) if doubles else 0
   pTriple = triples/float(plateAppearences) if triples else 0
   pHR = hr/float(plateAppearences) if hr else 0
   pOut = 1 - ((singles+doubles+triples+hr + walks)/float(plateAppearences)) if singles+doubles+triples+hr+walks else 0
   pWalk = (walks + hbp)/float(plateAppearences) if walks+hbp else 0
   pWalkSingle = (walks+singles+hbp)/float(plateAppearences) if walks+singles+hbp else 0

   #print("Stats", pSingle, pDouble, pTriple, pHR, pWalkSingle, pOut, pWalk, (pSingle + pDouble + pTriple + pHR + pWalkSingle + pOut + pWalk))


   transition = numpy.matrix([
                              [pHR,pWalkSingle,pDouble,pTriple,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [pHR,0,0,pTriple,pWalkSingle,0,pDouble,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [pHR,pSingle,pDouble,pTriple,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [pHR,pSingle,pDouble,pTriple,0,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0,0],
                              [pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0,0],
                              [pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0,0],
                              [pHR,pSingle,pDouble,pTriple,0,0,0,pWalk,0,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0,0],
                              [pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,0,0,pOut,0,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,pWalkSingle,pDouble,pTriple,0,0,0,0,pOut,0,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pWalkSingle,0,pDouble,0,0,pOut,0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,pWalk,0,0,0,0,0,pOut,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,pWalk,0,0,0,0,0,pOut,0,0,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,pOut,0,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,pOut,0,0,0],
                              [0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,0,0,pWalk,0,0,0,0,0,0,pOut,0,0],
                              [0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,0,0,0,0,0,0,0,pOut,0],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pWalkSingle,pDouble,pTriple,0,0,0,0,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pWalkSingle,0,pDouble,0,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,pWalk,0,0,0,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,pWalk,0,0,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,pSingle,pDouble,pTriple,0,0,0,pWalk,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,pHR,0,0,pTriple,pSingle,0,pDouble,pWalk,pOut],
                              [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
                              ])

   runVector  = numpy.matrix([
                              [pHR],
                              [2*pHR + pTriple],
                              [2*pHR + pSingle + pDouble + pTriple],
                              [2*pHR + pSingle + pDouble + pTriple],
                              [3*pHR + pSingle + pDouble + 2*pTriple],
                              [3*pHR + pSingle + pDouble + 2*pTriple],
                              [3*pHR + 2*pSingle + 2*pDouble + 2*pTriple],
                              [4*pHR + 2*pSingle + 2*pDouble + 3*pTriple + pWalk],
                              [pHR],
                              [2*pHR + pTriple],
                              [2*pHR + pSingle + pDouble + pTriple],
                              [2*pHR + pSingle + pDouble + pTriple],
                              [3*pHR + pSingle + pDouble + 2*pTriple],
                              [3*pHR + pSingle + pDouble + 2*pTriple],
                              [3*pHR + 2*pSingle + 2*pDouble + 2*pTriple],
                              [4*pHR + 2*pSingle + 2*pDouble + 3*pTriple + pWalk],
                              [pHR],
                              [2*pHR + pTriple],
                              [2*pHR + pSingle + pDouble + pTriple],
                              [2*pHR + pSingle + pDouble + pTriple],
                              [3*pHR + pSingle + pDouble + 2*pTriple],
                              [3*pHR + pSingle + pDouble + 2*pTriple],
                              [3*pHR + 2*pSingle + 2*pDouble + 2*pTriple],
                              [4*pHR + 2*pSingle + 2*pDouble + 3*pTriple + pWalk],
                              [0]
                              ])

   resultMatrix = runVector
   for z in  range(1,12):
       curentTransition = linalg.matrix_power(transition, z)
       tempMatrix = numpy.dot(curentTransition,runVector)
       resultMatrix = numpy.add(resultMatrix,tempMatrix)

   return resultMatrix

statTotalArray = []
with open('stats.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
          statTotalArray.append(
          {
             "year": int(row[0]),
             "rpg": float(row[1]),
             "pa": int(row[2]),
             "singles": int(row[3])-int(row[4])-int(row[5])-int(row[6]),
             "doubles": int(row[4]),
             "triples": int(row[5]),
             "hr": int(row[6]),
             "bb": int(row[7]),
             "hbp": int(row[8])
          })
x=[]
y=[]
for row in statTotalArray:
    x.append(perGameMarkovRuns(row))
    y.append(row["rpg"])
m=numpy.array(y[:len(y)-1])
n=numpy.array(y[1:])
x=numpy.array(x)
y=numpy.array(y)
slope, intercept, r_value, p_value, std_err = stats.linregress(n,m)


# Calculate some additional outputs
predict_y = intercept + slope * x

pred_error = y - predict_y
degrees_of_freedom = len(x) - 2
residual_std_error = numpy.sqrt(numpy.sum(pred_error**2) / degrees_of_freedom)

print pred_error, " , ", std_err, " , ", residual_std_error, " , ", degrees_of_freedom
# Plotting
ppl.plot(x, y, 'o')
ppl.plot(m, n, 'o')

ppl.plot(x, predict_y, label=str("mRuns vs Hist"))

slope0, intercept0, r_value0, p_value0, std_err0 = stats.linregress(m,n)
print "mRuns vs rpg r-squared:", r_value0**2, std_err0, 


# Calculate some additional outputs
predict_n = intercept0 + slope0 * m
ax = ppl.plot(m, predict_n, label=str("Hist vs Hist(n-1)"))
ppl.legend(ax, loc='lower left', ncol=4)


mpld3.show()