import math
import sys

mp = dict()
def cos(x):
    return math.cos((x * math.pi) / 180)
def sin(x):
    return math.sin((x * math.pi) / 180)

for i in sys.stdin:
    if i[0:-1] == "bye()":
        break
    elif i[0:6] == "print(":
        print(mp[i[6:-2]])
    else:
        tmp = i.split("<-")
        mp[tmp[0]] = eval(tmp[1], mp, locals())