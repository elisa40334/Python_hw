class treeNode:
    def __init__(self, name, nodeCount, parentNode):
        self.name = name # 节点元素名称
        self.cal = nodeCount # 节点出现的次数
        self.nodeLink = None # 指向下一个相似节点
        self.parent = parentNode # 指向父节点
        self.children = {} # 指向子节点，子节点元素名称为键，指向子节点指针为值
    def count(self, nodeCount):
        """
        增加节点的出现次数
        :param nodeCount:
        :return:
        """
        self.cal += nodeCount

    def disp(self, ind=1):
        """
        输出节点和子节点的FP树结构
        :param ind:
        :return:
        """
        print('  ' * ind, self.name, ' ', self.count) # 展示节点名称和出现的次数
        for child in self.children.values():
            child.disp(ind + 1) #打印时，子节点的缩进比父节点更深一级


def addNode(item, tree, dict, count):
    if item[0] in tree.children:
        tree.children[item[0]].count(count)
    else:
        # 如果不存在子节点，我们为该inTree添加子节点
        tree.children[item[0]] = treeNode(item[0], count, tree)
        # 如果满足minSup的dist字典的value值第二位为null， 我们就设置该元素为 本节点对应的tree节点
        # 如果元素第二位不为null，我们就更新header节点
        if dict[item[0]][1] is None: #如果在相似元素的字典headerTable中，该元素键对应的列表值中，起始元素为None
            # headerTable只记录第一次节点出现的位置
            dict[item[0]][1] = tree.children[item[0]] #把新创建的这个节点赋值给起始元素
        else:
            # 本质上是修改headerTable的key对应的Tree，的nodeLink值
            # 如果在相似元素字典headerTable中，该元素键对应的值列表中已经有了起始元素，那么把这个新建的节点放到值列表的最后
            updateHeader(dict[item[0]][1], tree.children[item[0]])
    if len(item) > 1:
        # 递归的调用，在items[0]的基础上，添加item0[1]做子节点， count只要循环的进行累计加和而已，统计出节点的最后的统计值。
        addNode(item[1::], tree.children[item[0]], dict, count)
def updateHeader(nodeToTest, targetNode):
    """
    更新项头表：
    项头表可以使遍历树更加快速，它是一个横向迭代向前并判断的思想。
    更新头指针表，确保节点链接指向树中该元素项的每一个实例
    (更新头指针，建立相同元素之间的关系，
    例如:  左边的r指向右边的r值，就是后出现的相同元素 指向 已经出现的元素)
    从头指针的nodeLink开始，一直沿着nodeLink直到到达链表末尾。这就是链表。
    性能: 如果链表很长可能会遇到迭代调用的次数限制。
    :param nodeToTest: 满足minSup {所有的元素+(value, treeNode)}
    :param targetNode: Tree对象的子节点
    :return:
    """

    while nodeToTest.nodeLink is not None:
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

 
data1 = [
        ['A', 'B', 'C', 'E', 'F','O'],
        ['A', 'B', 'C', 'E', 'F','O'],
        ['A', 'C', 'G'],
        ['E','I'],
        ['A', 'C', 'D', 'E', 'G'],
        ['A', 'C', 'E', 'G', 'L'],
        ['E', 'J'],
        ['A', 'B', 'C', 'E', 'F', 'P'],
        ['A', 'C', 'D'],
        ['A', 'C', 'E', 'G', 'M'],
        ['A', 'C', 'E', 'G', 'N']]

dict = {} #用來存放item在各個itemset中出現的次數
for i in data1: #用來計算item在各個itemset中出現的次數
    for j in i:
        if j in dict:
            dict[j] += 1
        else:
            dict[j] = 1
dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1],reverse = True)} #根據出現次數sorting
data2 = [] #用來裝按照元素出現頻率重新排列的itemset
for i in data1:
    data2.append([x for x in dict.keys() if x in i])
dict = {k: v for k, v in dict.items() if v >= len(data1)*0.2} #滿足support >= 0.2

top = treeNode("Top",1,None)
data2set = []
for i in data2:
    if i not in data2set:
        data2set.append(i)

# data2dict = {}
# for i in data2set:
#     if i not in data2dict:
#         data2dict[frozenset(i)] = 1
#     else:
#         data2dict[frozenset(i)] += 1
for i in data2set:
    print(i)
    # addNode(i, top, dict, data2.count(i))
print(data2set)
for a,b in dict.items():
    print(a,b)
    
top.disp()

