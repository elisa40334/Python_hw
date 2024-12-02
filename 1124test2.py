import pandas as pd
from mlxtend.preprocessing import TransactionEncoder  # 传入模型的数据需要满足特定的格式，可以用这种方法来转换为bool值，也可以用函数转换为0、1
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

shopping_list = [['豆奶', '莴苣'],
                 ['莴苣', '尿布', '葡萄酒', '甜菜'],
                 ['豆奶', '尿布', '葡萄酒', '橙汁'],
                 ['莴苣', '豆奶', '尿布', '葡萄酒'],
                 ['莴苣', '豆奶', '尿布', '橙汁']]

shopping_df = pd.DataFrame(shopping_list)

df_arr = shopping_df.stack().groupby(level=0).apply(list).tolist()

te = TransactionEncoder()  # 定义模型
df_tf = te.fit_transform(df_arr)
df = pd.DataFrame(df_tf, columns=te.columns_)

# 求频繁项集：
frequent_itemsets = fpgrowth(df, min_support=0.05, use_colnames=True)  # use_colnames=True 表示使用元素名字，默认的False使用列名代表元素
frequent_itemsets.sort_values(by='support', ascending=False, inplace=True)  # 频繁项集可以按支持度排序
print(frequent_itemsets[frequent_itemsets.itemsets.apply(lambda x: len(x)) >= 2])  # 选择长度 >=2 的频繁项集

# 求关联规则：
association_rule = association_rules(frequent_itemsets, metric='confidence',
                                     min_threshold=0.9)  # metric可以有很多的度量选项，返回的表列名都可以作为参数
association_rule.sort_values(by='leverage', ascending=False, inplace=True)  # 关联规则可以按leverage排序
print(association_rule)
