import random

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
        return temp

#####################################################################################

for probabilityLoop in range(1, 10):
    results = {}
    looprange = 1000
    probability = probabilityLoop/10.0
    sumTotalWeight = 0
    sumCount = 0

    for loop in range(looprange):
        weightList = []
        graphList = []
        MWIS = []
        randomState = []
        currentState = []
        lastState = []
        stopState = []
        totalWeight = 0
        ranInOut = [0, 1]
        infiniteFlag = False

        file = open('test2.txt', 'r')      #you can modify testfile here
        for i,line in enumerate(file):
            if i == 1:
                for plot in line.split():
                    weightList.append( int(plot))
            elif i > 1:
                graphList.append( Node( i-2, weightList[i-2], list( map( int, line.split()))))
                stopState.append(-1)
                currentState.append(random.choice(ranInOut))
        file.close()

        ######################################################################################
        count = 0
        randomState = currentState[:]

        while currentState !=  stopState:
            lastState = currentState[:]
            for i in range(10):
                if random.random() <= probability :
                    randomState[i] = 1
                else:
                    randomState[i] = 0  

            for node in graphList:  
                if randomState[node.index] == 1 :
                    for adjNode in node.getAdjNode():
                        if lastState[adjNode] == 1 and node.weightPerNumPlusOne <= graphList[adjNode].weightPerNumPlusOne:
                            flag = 0
                            break
                        else:
                            flag = 1
                    if flag == 1:
                        currentState[node.index] = 1
                    elif flag == 0:
                        currentState[node.index] = 0   

            for node in graphList:
                for adjNode in node.getAdjNode():
                    if currentState[adjNode] == 1 and node.weightPerNumPlusOne <= graphList[adjNode].weightPerNumPlusOne:
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag == 1:
                    stopState[node.index] = 1
                elif flag == 0:
                    stopState[node.index] = 0
            if count > len(currentState)*100:
                infiniteFlag = True
                break
            count += 1

        #for i in graphList:
        # print(i.index, i.weight , i.adjVec, i.adjNum, i.weightPerNumPlusOne)
        #print(currentState)

        for i,choose in enumerate(currentState):
            if choose == 1:
                MWIS.append(i)
                totalWeight += graphList[i].weight
        # print(MWIS)
        # print(totalWeight)
        sumTotalWeight += totalWeight
        sumCount += count
        resultState = tuple(MWIS)
        if infiniteFlag:
            if results.get('infinite') == None:
                results['infinite'] = 1
            else:
                results['infinite'] += 1
        else:
            if results.get(resultState) == None:    
                results[resultState] = 1
            else:
                results[resultState] += 1
    print("probability",probability)
    for key,value in results.items():
        print(str(key) + " : " + str(value/looprange))
    print("averaged total weight", sumTotalWeight/looprange)
    print("averaged convergence time", sumCount/looprange)

