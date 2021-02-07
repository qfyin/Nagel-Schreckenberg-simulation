from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

seed = None  # Current system time is used as the seed

lanes = 3
length = 330 # 1600m, 5m/block

maxSpeed = 5
maxLength = 10000

# Tsinghua West Entrance: 75 seconds Green, then 115 Red
# A weekend noon: 20 ±5 cars in a round (190 second)

trafficLight1 = SpeedLimit(range=((100,0), (100,2)), limit=0, ticks=90 * 1000 / updateFrame, active=False)
QHFZ1 = SpeedLimit(range=((230,1), (245,1)), limit=2, ticks=0)
QHFZ2 = SpeedLimit(range=((235,2), (245,2)), limit=1, ticks=0)
trafficLight2 = SpeedLimit(range=((320,0), (320,2)), limit=0, ticks=90 * 1000 / updateFrame, active=False)

speedLimits = [ trafficLight1, QHFZ1, QHFZ2, trafficLight2 ]
# trafficGenerator = SimpleTrafficGenerator(1)
carPerMinute = 20
trafficGenerator = PoissonTrafficGenerator(carPerMinute * updateFrame / (60 * 1000))
slowDownProbability, laneChangeProbability = 0.4, 0.8
