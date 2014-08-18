import numpy
from numpy import linalg

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
