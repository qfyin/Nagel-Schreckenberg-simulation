import random


class SimpleTrafficGenerator():
    def __init__(self, carPerUpdate=1):
        self.queue = 0
        self.carPerUpdate = carPerUpdate

    def generate(self, road):
        amount = random.randint(0, self.carPerUpdate)
        self.tryGenerate(road, amount)

    def tryGenerate(self, road, amount):
        added = road.pushCarsRandomly(amount + self.queue)
        self.queue += (amount - added)

#P(x=k) = λ^k*e^(-λ)/k!

# algorithm poisson random number (Knuth):
#    init:
#         Let L ← e^{−λ}, k ← 0 and p ← 1.
#    do:
#         k ← k + 1.
#         Generate uniform random number u in [0,1] and let p ← p × u.
#    while p > L.
#    return k − 1.

class PoissonTrafficGenerator():
    def __init__(self, carPerUpdate = 1):
        self.queue = 0
        self.carPerUpdate = carPerUpdate
        self.nextOccur = random.expovariate(self.carPerUpdate)

    def generate(self, road):
        self.nextOccur -= 1
        amount = 0
        while (self.nextOccur < 0):
            amount += 1
            self.nextOccur += random.expovariate(self.carPerUpdate)
        self.tryGenerate(road, amount)

    def tryGenerate(self, road, amount):
        added = road.pushCarsRandomly(amount + self.queue)
        self.queue += (amount - added)
