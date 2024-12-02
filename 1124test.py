from itertools import combinations
from collections import OrderedDict
import numpy as np
a = [{'b','a','d','c'},{'a','b','c'},{'g','b'},{'g'}]
b = [1,4,2]
c = {frozenset({'b','a','d','c'}):1,frozenset({'a','b','c'}):4,frozenset({'g'}):2,frozenset({'g','b'}):6}
ans = 0
for i in a:
    subsets = [x for x in a if (i & x == x) and x != i] 
    for j in subsets:
        if (c[frozenset(j)] / c[frozenset(i)] >= 0.8):
            ans += 1
print(ans)
# print( sorted(c), sorted(c[0]))
# c.sort(key=len,reverse=True)
# print(c)
# k = list(map(lambda x:len(x),a))
# print(k)
# a.sort(key=len,reverse=True)
# b = [x for _,x in sorted(zip(len,b))]
# # b = list(map(lambda x:))
# # b = np.lexsort(b,k)
# print(a,b)
# print(a[1] & a[0])