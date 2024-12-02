'''
Frequent Pattern Tree 繁模式树

牛奶 a   面包 b   尿布 c   啤酒 d   可乐 e   鸡蛋 f
所用数据集
T1  {牛奶,面包}
T2  {面包,尿布,啤酒,鸡蛋}
T3  {牛奶,尿布,啤酒,可乐}
T4  {面包,牛奶,尿布,啤酒}
T5  {面包,牛奶,尿布,可乐}
   转化为字母表示，即
数据集
database = [    ['a', 'b'],
                ['b', 'c', 'd', 'f'],
                ['a', 'c', 'd', 'e'],
                ['b', 'a', 'c', 'd'],
                ['b', 'a', 'c', 'e']   ]
'''
class FpNode():

    def __init__(self, name='', childs={}, parent={}, nextCommonId={}, idCount=0):
        self.idName = name  # 名字
        self.childs = childs  # 所有孩子结点
        self.parent = parent  # 父节点
        self.nextCommonId = nextCommonId  # 下一个相同的 id名字 结点
        self.idCount = idCount  # id 计数

    def getName(self):      #获取该节点名字
        return self.idName

    def getAllChildsName(self):     #获取该节点所有孩子节点的名字
        ch = self.childs
        keys = list(ch.keys())
        names = []
        for i in keys:
            names.append( list(i))
        return names

    def printAllInfo(self):     #打印该节点所有信息
        print(self.idName, self.idCount, list(self.childs.keys()), list(self.parent.keys()), self.nextCommonId.items() )

    @classmethod
    def checkFirstTree(cls, rootNode):   #前序遍历整个树（这不是二叉树，没有中序遍历）
        if rootNode is None:
            return ''
        #parent1 = rootNode.parent.keys()      #要加一个 强转 ，否则它会变成 Nopetype 型，
        rootNode.printAllInfo()       # print(rootNode.idName, type(rootNode.parent))  报错 root <class 'NoneType'>

        if rootNode.childs is not None:
            keys = list(rootNode.childs.keys())
            for i in keys:
                cls.checkFirstTree(rootNode.childs[i])

    @classmethod
    def checkBehindTree(cls, rootNode):     #后序遍历整个树
        if rootNode is None:
            return ''
        if rootNode.childs is not None:
            keys = list(rootNode.childs.keys())
            for i in keys:
                cls.checkBehindTree(rootNode.childs[i])
        rootNode.printAllInfo()



import copy

def scan1_getCand1(database): #第一次扫描统计出现的次数
    c1 = {}  #候选集

    for i in database:
        for j in i:
            c1[j] = c1.get(j, 0) + 1        #表示如果字典里面没有想要的关键词，就返回0
    #print(c1)
    return c1

#返回排好序的字典

#对数据进行排序，按支持度由大到小排列
def sortData(**d):    #形参前添加两个 '*'——字典形式  形参前添加一个 '*'——元组形式
    sortKey = list(d.keys())               #直接使用sorted(my_dict.keys())就能按key值对字典排序
    sortValue = list(d.values())

    length = len(sortKey)
    for i in range(length-1):   #按照支持度大小，由大到小排序的算法
        for j in (i, length-1-1):  #必须 -1 （1，len）虽然不包含 len本身 但是数组【len-1】时最后一个元素，必须减去这个元素
            if sortValue[i] < sortValue[j + 1]:
                sortValue[i], sortValue[j + 1] = sortValue[j + 1], sortValue[i]     #如果它的支持度小与另一个，交换位置
                sortKey[i], sortKey[j + 1] = sortKey[j + 1], sortKey[i]

    new_c1 = {}     #存放排完序的数据记录
    for i in range(length):
        new_c1[sortKey[i]] = sortValue[i]

    return new_c1  #返回排好序的字典

#得到 database 的频繁项集
def  getFreq(database, minSup = 3, **c1):   #返回频繁项集，和频繁项集的支持度

    c1 = scan1_getCand1(database)        #第一次扫面数据库，求第一次候选集，返回的是字典
    new_c1 = sortData(**c1)      #排序，大到小

    keys = list(new_c1.keys())
    for i in keys:
        if new_c1[i] < minSup:  #若支持度小于最小支持度，则删除该商品
            del new_c1[i]

    f1 = []  # 第一次频繁项集
    new_keys = list(new_c1.keys())
    for i in new_keys:
        if [i] not in f1:
            f1.append( [i] )  #每个元素自成一项
    #print(f1,new_c1)
    return f1, new_c1

def createRootNode():   #创建一个根节点
    rootNode = FpNode('root', {}, {}, {}, -1)     #name, childs, parent, nextCommonId, idCount
    return rootNode

def buildTree(database, rootNode, f1):   #构建频繁模式树 FpTree

    for i in database:  #第二次扫描数据库
        present = rootNode  #指向当前节点
        next = FpNode(name='', childs={}, parent={}, nextCommonId={}, idCount=0) #创建一个新节点，并初始化
        for j in f1:  #按支持度从大到小的顺序进行构建节点
            if set(j).issubset(set(i)): #j如果在i里面
                if (present.getName() is 'root') and j not in rootNode.getAllChildsName():
                    next.idName = str(j[0])     #对新创建的节点进行赋值
                    next.idCount = next.idCount + 1
                    next.nextCommonId = {str(j[0]): 0}

                    next.parent.update({rootNode.idName:rootNode})
                    temp = copy.copy(next)
                    rootNode.childs.update({str(j[0]):temp})  #往它插入父亲节点
                    ##print(temp.parent)

                    present = temp         #present = next 这样直接赋值是 引用 ，一定要注意
                    next = FpNode(name='', childs={}, parent={}, nextCommonId={}, idCount=0)  #创建并初始化下一个新节点

                else:
                    if j in present.getAllChildsName():     #如果需要插入的节点已经存在
                        temp2 = present.childs[str(j[0])]
                        present = temp2
                        present.idCount = present.idCount + 1   #count+1即可
                    else:
                        next.idName = str(j[0])         #对新插入的节点赋值
                        next.idCount = next.idCount + 1
                        next.nextCommonId = {str(j[0]): 0}
                        next.parent.update({present.idName:present})
                        #temp3 = copy.copy(next)
                        present.childs.update({str(j[0]):next})     #往它插入父亲节点
                        #temp3.childs = {}

                        present = next
                        next = FpNode(name='', childs={}, parent={}, nextCommonId={}, idCount=0)

                #present = next
                #next = FpNode()
    #print(rootNode.getAllChildsName())
    # print('前序遍历如下：')
    # FpNode.checkFirstTree(rootNode)
    # print('后序遍历如下：')
    # FpNode.checkBehindTree(rootNode)
    return None

#构建线索，填节点的nextCommonId这个属性
def buildIndex(rootNode, d1):  #传 列表或字典时，列表前，加*， 字典前加 ** 表示传给函数的是一个地址，在函数内部改变这个参数，不会影响到函数外的变量

    if rootNode is None:
        return ''
    next = rootNode   #指向下一个节点，当前赋值为根节点
    value = rootNode.idName
    #print(value)
    #print(d1[str(value)])             #d1[value] {KeyError}'a'???????????????   如果value是根节点root，就会出错，表中本来就没有root这个值
    #print(d1)
    if value != 'root':
        indexAds1 = {value: d1[value]}
        if d1[value] == 0:  # 线索构造   我已经把初始化了所有的 nextCommonId 为 {'': 0}
                                    # 所以后面只要 这个节点的 nextCommonId字典的值为0，就说明这个字典就是构建的链表链尾
            d1[value] = next
            # print(indexAds1)
        else:
            while  indexAds1[value] != 0:
                indexAds1 = indexAds1[value].nextCommonId       #以链表形式把最后一个 表尾元素找出来
                #print(indexAds1)
            indexAds1[value] = next  #这个元素后面加入 当前所在树的这个节点的地址
            #print(next.nextCommonId)
    if rootNode.childs is not None:     #根节点孩子不是null，则对它的每个孩子，依次递归进行线索构建
        keys = list(rootNode.childs.keys())
        for i in keys:
            buildIndex(rootNode.childs[i], d1)

def createIndexTableHead(**indexTableHead):     #创建一个表头，用来构建线索，表头的名字是相应节点的名字
    keys = list(indexTableHead.keys())
    #print(keys)
    for i in keys:
        indexTableHead[i] = 0

    return indexTableHead

def getNewRecord(idK, **indexTableHead):        #得到新的数据记录
    newData = []
    address = indexTableHead[idK]

    while address != 0:
        times = 0
        times = address.idCount  #当前节点count数
        l = []  #临时存放这个分支上的所有节点元素，单个单个存储 二维列表
        getOneNewR = [] #和l一样，是l的倒叙，因为l本来是倒叙的，现在把它改成倒叙
        #print(list(address.parent.keys())[0])  #这样写才是 字符 c  而不是 'c'
        nextAdress = copy.copy(address)#一个指针，指向父亲节点，初始化为表头第一个的地址
        while list(nextAdress.parent.keys())[0] is not 'root':  #该节点发父亲节点不是根节点。则
            #print(address.parent)
            l.append(list(nextAdress.parent.keys()))    #把它的父亲节点加入l中

            parentIdName = list(nextAdress.parent.keys())[0]    #父亲节的名字
            nextAdress = nextAdress.parent[ parentIdName  ]  #指向该节点父亲节点
        if l != []:
            for j in l:
                getOneNewR.append(j[0])

        if getOneNewR != []:
            for k in range(times):    #若最后的那个 idk 计数为多次，要把它多次添加到新产生的newData中
                newData.append(list(getOneNewR))
         #把得到的记录加入新的数据集中

        address = address.nextCommonId[idK]  #指向下一个表头元素的开始地址，进行循环

    return newData

#    idK表示当前新产生的数据集是在去除这个字母后形成的，  fk是去除掉idk后，新的第一次频繁项集  dk是fk的支持度
def getAllConditionBase(newDatabase,idK, fk, minSup, **dk): #返回条件频繁项集 base， 和支持度

    if fk != []:    #频繁项集非空
        newRootNode = createRootNode()  #创建新的头节点
        buildTree(newDatabase, newRootNode, fk)
        #newIndexTableHead = {}  #创建新表头
        newIndexTableHead = createIndexTableHead(**dk)  # **dk 就是传了个值，给了它一个拷贝，修改函数里面的这个拷贝，不会影响到外面的这个变量的值
        buildIndex(newRootNode, newIndexTableHead)
    else:
        return [idK], {idK:9999}    #频繁项集是空的，则返回idk的名字，支持度设为最大值9999，这样会出现一些问题，最后已经解决了，在主函数代码中有表现出来

    if len(newRootNode.getAllChildsName()) < 2: #新的FpTree只有1条分支，（这里只认为根节点只有1个孩子，就说他只有一条分支）
                                  #若是实际数据，就不能这样写了，应当在写一个函数，从根节点开始遍历，确保每个节点都只有1个孩子，才能认为只有1条分支
        base = [[]] #条件基
        node = newRootNode
        while node.getAllChildsName() != []:    #当前节点有孩子节点
            childName = list(node.childs.keys())        #一个列表，孩子节点的所有名字，其实就1个孩子，前面已经判断了是单节点
            base.append(list(childName[0]))   # 把孩子节点加入条件基
            #print(node.childs)
            #print(childName)
            node = node.childs[childName[0]] #指向下一个节点
        #print(base)
        itemSup = {node.idName : node.idCount}    #这一条分支出现的次数，最后求频繁项集支持度需要用到
        #print(itemSup)
        return base, itemSup #返回条件基，还有这一条分支出现的次数，
    else:   #分支不止1条，进行递归查找，重复最开始的操作
        base = [[]]
        for commonId in fk[-1::-1]: #倒叙进行
            newIdK = str(commonId[0])
            newDataK = getNewRecord(newIdK, **newIndexTableHead)  # 传入这个表头的一个拷贝
            fk2, dk2 = getFreq(newDataK, minSup)
            conditionBase, itemSup = getAllConditionBase(newDataK, newIdK, fk2, minSup, **dk2)   #得到该条件基下的条件基，及各个分支出现次数
                                                #递归进行
            base.append(conditionBase)

        return base, itemSup

#FpGrowth算法本身（Frequent Pattern Growth—-频繁模式增长）
def FpGrowth(database, minSup = 3):
    f1, d1 = getFreq(database, minSup)  #求第一次频繁项集,并返回一个字典存放支持度，且按大到小排序，返回频繁项和存放频繁项支持度的字典
    rootNode = createRootNode()  #创建根节点
    #print(f1,d1)        #[['a'], ['b'], ['c'], ['d']]      {'a': 4, 'b': 4, 'c': 4, 'd': 3}

    # 第一步建造树
    buildTree(database,rootNode, f1)
    #indexTableHead = {}     #创建线索的表头，一个链表
    indexTableHead =  createIndexTableHead(**d1)  # **d1 就是传了个值，给了它一个拷贝，修改函数里面的这个拷贝，不会影响到外面的这个变量的值
    buildIndex(rootNode, indexTableHead)   #创建线索，用这个表头

    # print('构建线索后，前序遍历如下：')
    # FpNode.checkFirstTree(rootNode)
    # print('构建线索后，后序遍历如下：')
    # FpNode.checkBehindTree(rootNode)

    freAll = []   #所有频繁项集
    freAllDic = {}  #所有频繁项集的支持度

    #第二步    进行频繁项集的挖掘，从表头header的最后一项开始。
    for commonId in f1[-1::-1]:      #倒叙 从支持度小的到支持度大的，进行挖掘
        idK = str(commonId[0])
        newDataK = getNewRecord(idK, **indexTableHead)    #传入这个表头的一个拷贝， 函数返回挖掘出来的新记录
        fk, dk = getFreq(newDataK, minSup)  #对新数据集求频繁项集
        #print(fk,dk)
        base,  itemSup= getAllConditionBase(newDataK, idK, fk, minSup, **dk)  #得到当前节点的条件频繁模式集，返回
        #有可能会发生这样一种情况，条件基是 a ，然后fk，dk为空，结果这个函数又返回了 a，那么最后的结果中，就会出现 a，a  这种情况，处理方法请往下看

        #print(base，idK)
        for i in base:
            #print(i)
            t = list(i)
            t.append(idK)
            t = set(t)      #为了防止出现 重复 的情况，因为我的getAllConditionBase(newDataK, idK, fk, minSup, **dk)方法的编写，可能会形成重复，如   a，a
            t = list(t)

            freAll.append(t)
            itemSupValue = list(itemSup.values())[0]

            x = tuple(t)  #列表不能做字典的关键字，因为他可变，，而元组可以
                                            #<class 'list'>: ['c', 'd']
            #print(t[0])     # t是列表，字典的关键字不能是可变的列表， 所以用 t[0] 来取出里面的值
            freAllDic[x] = min(itemSupValue, d1[idK])
    #print(freAll)
    #print(freAllDic)

    return freAll, freAllDic

if __name__ == '__main__':

    # database = [['a', 'b'],
    #             ['b', 'c', 'd', 'f'],
    #             ['a', 'c', 'd', 'e'],
    #             ['b', 'a', 'c', 'd'],
    #             ['b', 'a', 'c', 'e']]
    
    database = []
    fo = open("mushroom.dat", "r")
    for _ in range(8124):
        line = fo.readline().strip()
        database.append(line.split(" "))
    fo.close()
    minSup = 813
    
    # database = [['豆奶', '莴苣'],
    #              ['莴苣', '尿布', '葡萄酒', '甜菜'],
    #              ['豆奶', '尿布', '葡萄酒', '橙汁'],
    #              ['莴苣', '豆奶', '尿布', '葡萄酒'],
    #              ['莴苣', '豆奶', '尿布', '橙汁']]

    freAll, freAllDic = FpGrowth(database, minSup)
    #  minSup = 3     [['d'], ['d', 'c'], ['c'], ['c', 'a'], ['c', 'b'], ['b'], ['b', 'a'], ['a']]

    print(freAll)
    count = [0,0,0,0,0,0]
    print("各个频繁项集的支持度依次为：")
    for i in freAllDic.keys():
        print(i, freAllDic[i])
        # if len(i) == 1:
        #     count[1]+=1
        # elif len(i) == 2:
        #     count[2] += 1
        # elif len(i) == 3:
        #     count[3] += 1
        # elif len(i) == 4:
        #     count[4] += 1
        # elif len(i) == 5:
        #     count[5] += 1
# print(count[1],count[2],count[3],count[4],count[5])
            


