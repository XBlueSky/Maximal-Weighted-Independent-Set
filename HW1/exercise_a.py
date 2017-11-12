from operator import itemgetter, attrgetter

class Node:
    def __init__(self, index, weight, adjVec = []):
        self.index = index
        self.weight = weight
        self.adjVec = adjVec
        self.adjNum = 1
        for i in adjVec:
            if i == 1:
                self.adjNum += 1
        self.weightPerNumPlusOne = float(weight)/float(self.adjNum)

    def getAdjNode(self):
        temp = []
        for index,value in enumerate(self.adjVec):
            if value == 1:
                temp.append(index)
        temp.append(self.index)
        return temp

    def updateAdjNode(self, delNode = []):
        for i in delNode:
            self.adjVec[i] = 0
        self.adjNum = 1
        for i in self.adjVec:
            if i == 1:
                self.adjNum += 1
        self.weightPerNumPlusOne = float(self.weight)/float(self.adjNum)

#####################################################################################

weightList = [] 
graphList = []
MWIS = []

file = open('test2.txt', 'r')    #you can modify testfile here     
for i,line in enumerate(file):
    if i == 1:
        for plot in line.split():
            weightList.append( int(plot))
    elif i > 1:
        graphList.append( Node( i-2, weightList[i-2], list( map( int, line.split()))))
file.close()


graphList.sort(key = attrgetter('index'), reverse = True)
graphList.sort(key = attrgetter('weightPerNumPlusOne'))
graphList.reverse()

for i in graphList:
    print(i.index, i.weight , i.adjVec, i.adjNum, i.weightPerNumPlusOne)
totalWeight = 0
while len(graphList) > 0:
    MWIS.append(graphList[0].index)
    totalWeight += graphList[0].weight
    for j in graphList:
        if j.index != graphList[0].index:
            j.updateAdjNode(graphList[0].getAdjNode())
    for i in graphList[0].getAdjNode():
        for j in graphList:
            if i == j.index:
                graphList.remove(j)
    graphList.sort(key = attrgetter('index'), reverse = True)
    graphList.sort(key = attrgetter('weightPerNumPlusOne'))
    graphList.reverse()
    
MWIS.sort()
print(MWIS)
print(totalWeight)
#for i in graphList:
 #   print(i.index ,i.weight , i.adjVec, i.adjNum, i.weightPerNumPlusOne)




