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

#####################################################################################

weightList = []
graphList = []
MWIS = []
lastState = []
currentState = []
chooseVec = set()
totalWeight = 0

file = open('test1.txt', 'r')      #you can modify testfile here
for i,line in enumerate(file):
    if i == 1:
        for plot in line.split():
            weightList.append( int(plot))
    elif i > 1:
        graphList.append( Node( i-2, weightList[i-2], list( map( int, line.split()))))
        lastState.append(1)
        currentState.append(0)
file.close()

######################################################################################

while lastState !=  currentState:
    lastState = currentState[:]
    for node in graphList:
        for adjNode in node.getAdjNode():
            if lastState[adjNode] == 1 and node.weightPerNumPlusOne < graphList[adjNode].weightPerNumPlusOne:
                flag = 0
                break
            elif lastState[adjNode] and node.weightPerNumPlusOne == graphList[adjNode].weightPerNumPlusOne:
                if node.index > graphList[adjNode].index:
                    flag = 0
                    break
                else:
                    flag = 1
            else:
                flag = 1
        if flag == 1:
            currentState[node.index] = 1
        elif flag == 0:
            currentState[node.index] = 0
    print(currentState)
 #   for i in graphList:
  #      print(i.index, i.weight , i.adjVec, i.adjNum, i.weightPerNumPlusOne)
#print(currentState)

for i,choose in enumerate(currentState):
    if choose == 1:
        MWIS.append(i)
        totalWeight += graphList[i].weight
print(MWIS)
print(totalWeight)


