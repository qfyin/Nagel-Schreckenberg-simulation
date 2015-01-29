from simulation.speedLimits import *
from simulation.trafficGenerators import * 

maxFps= 40
size = width, heigth = 1280, 800
# in miliseconds
updateFrame = 500

lanes = 5
length = 200

maxSpeed = 5
maxLength = 10000

speedLimits = [ SpeedLimit( range=((100,1),(100,1)), limit=0, ticks=0, active=False),
        SpeedLimit( range=((130, 0), (170,0)), limit=0, ticks=0)
        ]
trafficGenerator = SimpleTrafficGenerator()
