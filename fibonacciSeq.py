class FibonacciSeq:
    def __init__(self, maxIteration):
        self.previousNum = 0
        self.nextNum = 1
        self.iterationCount = 0
        self.maxIteration = maxIteration

    def generateFibonacciSeq(self):
        while self.iterationCount <= self.maxIteration:
            print(self.previousNum)
            self.iterateFibonacciSequence()

    def iterateFibonacciSequence(self):
        self.previousNum, self.nextNum = self.nextNum, self.findNextNumber()
        self.iterationCount += 1

    def findNextNumber(self):
        return self.nextNum + self.previousNum


fs = FibonacciSeq(20)
fs.generateFibonacciSeq()
