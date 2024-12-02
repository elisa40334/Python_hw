import sys
import math
def bye():
    sys.exit()
def cos(x):
    return math.cos((x*math.pi)/180)
def sin(x):
    return math.sin((x*math.pi)/180)
var = []
val = []
while True:
    line = input()
    if line.find("<-") != -1:
        line = line.split("<-")
        var.append(line[0])
        for i in range(len(val)):
            if  line[1].find(var[i]) != -1:
                line[1] = line[1].replace(var[i],"val["+str(i)+"]")
        val.append(eval(line[1]))
    else:
        for i in range(len(val)): 
            if  line.find(var[i]) != -1: 
                line = line.replace(var[i],"val["+str(i)+"]") 
        eval(line)