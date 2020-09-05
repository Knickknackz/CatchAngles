import math

BioRowCatchDist = 4
BioRowFinishDist = 6
catchDistFromPin = BioRowCatchDist
finishDistFromPin = BioRowFinishDist
distInsideOarlock = .5
Spread = 84
catchAngle = 58
finishAngle = 32

def catchDistance(distFromPin, spread, catchAngle):
    extraDist = distFromPin / math.sin(math.radians(catchAngle))
    fullSpread = spread + extraDist
    return round(fullSpread * math.tan(math.radians(catchAngle)),2)

def finishDistance(distFromPin, spread, finishAngle):
    extraDist = distFromPin / math.sin(math.radians(finishAngle))
    shortSpread = spread - extraDist
    return round(shortSpread * math.tan(math.radians(finishAngle)),2)



print('---------------CATCH ANGLE DISTANCES---------------')
print(f'Outside Edge of Oar touches the centerline {catchDistance(catchDistFromPin, Spread, catchAngle)}cm away from the Line of the Pins')
print(f'"Middle" of the Oar touches the centerline  {catchDistance(catchDistFromPin/2, Spread, catchAngle)}cm away from the Line of the Pins')
print(f'Inside Edge of the Oar touches the centerline {catchDistance(distInsideOarlock, Spread, catchAngle)}cm away from the Line of the Pins')
print('\n')
print('---------------FINISH ANGLE DISTANCES---------------')
print(f'Outside Edge of Oar touches the centerline {finishDistance(finishDistFromPin, Spread, finishAngle)}cm away from the Line of the Pins')
print(f'"Middle" of the Oarlock touches the centerline {finishDistance(finishDistFromPin/2, Spread, finishAngle)}cm away from the Line of the Pins')
print(f'Inside Edge of the Oar touches the centerline {finishDistance(distInsideOarlock, Spread, finishAngle)}cm away from the Line of the Pins')
