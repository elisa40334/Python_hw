import itertools
import time


def get_time(func):
    """
    一个装饰器函数用于计算代码运行时间
    :param func:
    :return:
    """
    def fun(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('花费时间：', t)
        return ret
    return fun


class FPNode(object):
    """
    FP树节点，
    与pyfpgrowth库中基本一致
    """

    def __init__(self, value, count: int, parent):

        self.value = value
        self.count = count
        self.parent = parent
        self.next = None
        self.children = []

    def has_child(self, value) -> bool:

        for child in self.children:
            if value == child.value:
                return True
        return False

    def get_child(self, value):

        for child in self.children:
            if value == child.value:
                return child
        return None

    def add_child(self, value):
        new_child: FPNode = FPNode(value, 1, self)
        self.children.append(new_child)
        return new_child

    def __repr__(self):
        """
        这个是为了输出看着方便后加的
        :return:
        """

        return '<FPNode({}): {}>'.format(self.value, self.count)


class FPTree(object):

    def __init__(self, transactions, min_sup, root_value, root_count):

        self.frequent = self.find_frequent_items(transactions, min_sup)
        self.headers = self.build_header_table(self.frequent)
        self.root = self.build_fp_tree(transactions, self.frequent, self.headers, root_value, root_count)

    def show_header(self):
        """
        显示项头表
        :return:
        """

        for header in self.headers:
            node = self.headers[header]['header']
            while node is not None:
                print(node, node.parent, end=' -> ')
                node = node.next
            print('None')

    def not_empty(self):
        """
        判断FP树是否为空
        如果项头表为空，FP树必定为空
        :return:
        """

        return bool(self.headers)

    def build_fp_tree(self, transactions, frequent, headers, root_value, root_count):
        """
        建立FP树，填充项头表
        与pyfpgrowth库中基本一致
        :param transactions: 数据集
        :param frequent: 频繁一项集
        :param headers: 项头表
        :param root_value: 根节点的值
        :param root_count: 根节点支持度
        :return: FP树的根
        """

        root = FPNode(root_value, root_count, None)
        # 获取按支持度计数从大到小排序后的项的列表
        order_list = sorted(frequent.keys(), key=lambda k: frequent[k], reverse=True)

        for transaction in transactions:

            sorted_items = [item for item in transaction if item in frequent]
            sorted_items.sort(key=lambda item: order_list.index(item))
            if sorted_items:
                self.insert_tree(sorted_items, root, headers)

        return root

    @staticmethod
    def build_header_table(frequent):
        """
        建立项头表
        与pyfpgrowth库中基本一致
        项头表结构:
        headers = {
            item : {
                'header': FPNode(),
                'counter': 支持度计数
            }
        }
        :param frequent: 频繁一项集
        :return:
        """
        headers = {}
        for header in frequent.keys():
            headers[header] = {}
            headers[header]['header'] = None
            headers[header]['counter'] = 0
        return headers

    @staticmethod
    def find_frequent_items(transactions, min_sup):
        """
        找出所有频繁一项集
        与pyfpgrowth库中基本一致
        :param transactions: 数据集
        :param min_sup: 最小支持度
        :return:
        """
        items = {}
        for transaction in transactions:
            for item in transaction:
                if item not in items:
                    items[item] = 1
                else:
                    items[item] += 1
        items = {item[0]: item[1] for item in items.items() if item[1] >= min_sup}
        return items

    def insert_tree(self, items, node: FPNode, headers):
        """
        向FP树中插入一个数据项
        与pyfpgrowth库中基本一致
        :param items: 一个数据项
        :param node: 当前根节点
        :param headers: 项头表
        :return:
        """

        first = items[0]
        child: FPNode = node.get_child(first)
        if child:
            child.count += 1
            headers[first]['counter'] += 1
        else:
            child = node.add_child(first)
            header: FPNode = headers[first]['header']
            if header:
                while header.next:
                    header = header.next
                header.next = child

            else:
                headers[first]['header'] = child
            headers[first]['counter'] += child.count

        remaining_items = items[1:]
        if remaining_items:
            self.insert_tree(remaining_items, child, headers)

    def mine_patterns(self, min_sup):
        """
        得到所有频繁项集
        :return:
        """
        patterns = []  # 用于记录所有出现过的项集以及支持度计数

        self.mine_sub_trees(min_sup, set(), patterns)

        all_frequent_item_set = {}
        for item, support in patterns:
            if item not in all_frequent_item_set:
                all_frequent_item_set[item] = support
            else:
                all_frequent_item_set[item] += support

        # 对不符合最小支持度计数的项集进行筛选
        all_frequent_item_set = {item[0]: item[1] for item in
                                 sorted(all_frequent_item_set.items(), key=lambda item: len(item[0]))
                                 if item[1] >= min_sup}
        return all_frequent_item_set

    def mine_sub_trees(self, min_sup, frequent: set, patterns):
        """
        挖掘所有频繁项集
        这段代码借鉴于 https://blog.csdn.net/songbinxu/article/details/80411388
        中的mineFPtree方法
        :param min_sup: 最小支持度
        :param frequent: 前置路径
        :param patterns: 频繁项集
        :return:
        """

        # 最开始的频繁项集是headerTable中的各元素
        for header in sorted(self.headers, key=lambda x: self.headers[x]['counter'], reverse=True):
            new_frequent = frequent.copy()

            new_frequent.add(header)  #

            patterns.append((tuple(sorted(new_frequent)), self.headers[header]['counter']))

            condition_mode_bases = self.get_condition_mode_bases(header)

            condition_fp_tree = FPTree(condition_mode_bases, min_sup, header, self.headers[header]['counter'])
            # 继续挖掘
            if condition_fp_tree.not_empty():
                condition_fp_tree.mine_sub_trees(min_sup, new_frequent, patterns)

    def get_condition_mode_bases(self, item):
        """
        获取条件模式基
        与pyfpgrowth库中基本一致
        :param item: 项头表节点
        :return:
        """
        suffixes = []
        conditional_tree_input = []
        node = self.headers[item]['header']

        while node is not None:
            suffixes.append(node)
            node = node.next

        for suffix in suffixes:
            frequency = suffix.count
            path = []
            parent = suffix.parent

            while parent.parent is not None:
                path.append(parent.value)
                parent = parent.parent
            if path:
                path.reverse()
                for i in range(frequency):
                    conditional_tree_input.append(path)

        return conditional_tree_input

    def tree_has_single_path(self, root: FPNode):
        """
        判断树是否为单一路径
        与pyfpgrowth库中基本一致
        :param root: 根节点
        :return:
        """
        if len(root.children) > 1:
            return False
        elif len(root.children) == 0:
            return True
        else:
            self.tree_has_single_path(root.children[0])


@get_time
def find_frequent_patterns(transactions, min_sup):
    """
    寻找频繁项集
    与pyfpgrowth库中基本一致
    """
    tree = FPTree(transactions, min_sup, None, None)
    return tree.mine_patterns(min_sup)


def get_subset(frequent_set):
    """
    获取一个频繁项集的所有非空真子集
    注意: 这是个生成器
    :param frequent_set: 频繁项集
    :return:
    """
    length = len(frequent_set)
    for i in range(2 ** length):
        sub_set = []
        for j in range(length):
            if (i >> j) % 2:
                sub_set.append(frequent_set[j])
        if sub_set and len(sub_set) < length:
            yield tuple(sub_set)


def generate_association_rules(patterns, min_conf):
    """
    每条队则的样式： X->Y,  support = 支持度计数,  conf = s(X∪Y)/ s(X) = 可信度(百分比形式)
    :param patterns: 所有的频繁项集
    :param min_conf: 最小可信度（0~1）
    :return:
    """

    rules = []
    frequent_item_list = []

    # 对所有频繁项集进行归类
    for pattern in patterns:
        try:
            frequent_item_list[len(pattern) - 1][pattern] = patterns[pattern]
        except IndexError:
            for i in range(len(pattern) - len(frequent_item_list)):
                frequent_item_list.append({})
            frequent_item_list[len(pattern) - 1][pattern] = patterns[pattern]

    # 生成关联规则
    for i in range(1, len(frequent_item_list)):
        for frequent_set in frequent_item_list[i]:
            for sub_set in get_subset(frequent_set):
                frequent_set_support = frequent_item_list[i][frequent_set]
                sub_set_support = frequent_item_list[len(sub_set) - 1][sub_set]
                conf = frequent_set_support / sub_set_support
                if conf >= min_conf:
                    rest_set = tuple(sorted(set(frequent_set) - set(sub_set)))
                    rule = "{}->{}, support = {}, conf = {}/{} = {:.2f}%".format(
                        sub_set, rest_set, frequent_set_support, frequent_set_support, sub_set_support, conf * 100)
                    if rule not in rules:
                        rules.append(rule)
    return rules


if __name__ == '__main__':

    item_sets = []
    fo = open("mushroom.dat", "r")
    for _ in range(10):
        line = fo.readline().strip()
        item_sets.append(line.split(" "))
    fo.close()

    # item_sets = [
    #     ['f', 'a', 'c', 'd', 'g', 'i', 'm', 'p'],
    #     ['a', 'b', 'c', 'f', 'l', 'm', 'o'],
    #     ['b', 'f', 'h', 'j', 'o', 'w'],
    #     ['b', 'c', 'k', 's', 'p'],
    #     ['a', 'f', 'c', 'e', 'l', 'p', 'm', 'n']
    # ]

    frequent_patterns = find_frequent_patterns(item_sets, 3)
    # for frequent_pattern in generate_association_rules(frequent_patterns, 0):
    #     print(frequent_pattern)
    print("end")