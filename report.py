# coding:utf-8
count = [0,0,0,0,0,0]
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None
        self.parent = parentNode
        self.children = {}
    
    def inc(self, numOccur):
        self.count += numOccur
    
    def disp(self, ind=1):
        print('  '*ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind+1)

def updateHeader(nodeToTest, targetNode):
    while nodeToTest.nodeLink != None:
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode
def updateFPtree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        # 判断items的第一个结点是否已作为子结点
        inTree.children[items[0]].inc(count)
    else:
        # 创建新的分支
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    # 递归
    if len(items) > 1:
        updateFPtree(items[1::], inTree.children[items[0]], headerTable, count)

def createFPtree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in list(headerTable.keys()):
        if headerTable[k] < minSup:
            del(headerTable[k]) # 删除不满足最小支持度的元素
    freqItemSet = set(headerTable.keys()) # 满足最小支持度的频繁项集
    if len(freqItemSet) == 0:
        return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None] # element: [count, node]
    
    retTree = treeNode('Null Set', 1, None)
    for tranSet, count in dataSet.items():
        # dataSet：[element, count]
        localD = {}
        for item in tranSet:
            if item in freqItemSet: # 过滤，只取该样本中满足最小支持度的频繁项
                localD[item] = headerTable[item][0] # element : count
        if len(localD) > 0:
            # 根据全局频数从大到小对单样本排序
            orderedItem = [v[0] for v in sorted(localD.items(), key=lambda p:(p[1], str(p[0])), reverse=True)]
            #orderedItem = [v[0] for v in sorted(localD.items(), key=lambda p:(p[1], int(p[0])), reverse=True)]
            # 用过滤且排序后的样本更新树
            updateFPtree(orderedItem, retTree, headerTable, count)
    return retTree, headerTable

# 回溯
def ascendFPtree(leafNode, prefixPath):
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendFPtree(leafNode.parent, prefixPath)
# 条件模式基
def findPrefixPath(basePat, myHeaderTab):
    treeNode = myHeaderTab[basePat][1] # basePat在FP树中的第一个结点
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendFPtree(treeNode, prefixPath) # prefixPath是倒过来的，从treeNode开始到根
        if len(prefixPath) >= 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count # 关联treeNode的计数
        treeNode = treeNode.nodeLink # 下一个basePat结点
    return condPats

def mineFPtree(inTree, headerTable, minSup, preFix, freqItemList):
    # 最开始的频繁项集是headerTable中的各元素
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p:str(p[1]))] # 根据频繁项的总频次排序
    # print("bigL",bigL)
    for basePat in bigL: # 对每个频繁项
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        if len(newFreqSet) <= 5:
            freqItemList.append(newFreqSet)
            if len(newFreqSet) == 1:
                count[1] += 1
            elif len(newFreqSet) == 2:
                count[2] += 1
            elif len(newFreqSet) == 3:
                count[3] += 1
            elif len(newFreqSet) == 4:
                count[4] += 1
            elif len(newFreqSet) == 5:
                count[5] += 1
            condPattBases = findPrefixPath(basePat, headerTable) # 当前频繁项集的条件模式基
            myCondTree, myHead = createFPtree(condPattBases, minSup) # 构造当前频繁项的条件FP树
            if myHead != None:
                # print 'conditional tree for: ', newFreqSet
                # myCondTree.disp(1)
                mineFPtree(myCondTree, myHead, minSup, newFreqSet, freqItemList) # 递归挖掘条件FP树

def loadSimpDat():
    simpData = []
    fo = open("mushroom.dat", "r")
    for _ in range(8124):
        line = fo.readline().strip()
        simpData.append(line.split(" "))
    fo.close()
    return simpData
def createInitSet(dataSet):
    retDict={}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict
# def confidence(freqItemList, con):
#     for i in range(len(freqItemList)):
#         for j in range(i+1,len(freqItemList)):
#             if set(list(freqItemList[i])) & set(list(freqItemList[j])) == freqItemList[i]:
                
#             else if set(list(freqItemList[i])) & set(list(freqItemList[j])) == freqItemList[j]:

simpData = loadSimpDat() # load样本数据
#print(simpData, '\n')
# frozen set 格式化 并 重新装载 样本数据，对所有的行进行统计求和，格式: {行: 出现次数}
initSet = createInitSet(simpData)
#print(initSet,'\n')
minSup = 813
myFPtree, myHeaderTab = createFPtree(initSet, minSup)
# myFPtree.disp()

# part 5 : 创建条件模式基
freqItemList = []
mineFPtree(myFPtree, myHeaderTab, minSup, set([]), freqItemList)
print(myHeaderTab)
print(count[0],count[1],count[2],count[3],count[4],count[5])

print(freqItemList)
# freqItemList = confidence(freqItemList, 0.8)
