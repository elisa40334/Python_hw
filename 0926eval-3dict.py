import sys
import math
def bye():
    sys.exit()
def cos(x):
    return math.cos((x*math.pi)/180)
def sin(x):
    return math.sin((x*math.pi)/180)
dict = {}
for line in sys.stdin:
    if line.find("<-") != -1:
        line = line.split("<-")
        for k,v in dict.items():
            if line[1].find(k) != -1:
                line[1] = line[1].replace(str(k),str(v))
        dict[line[0]] = eval(line[1])
    else:
        for k,v in dict.items():
            if line.find(k) != -1:
                line = line.replace(str(k),str(v))
        eval(line) 