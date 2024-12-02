import sys  
import math  
def bye():  
    sys.exit()  
def cos(x):  
    return math.cos((x*math.pi)/180)  
def sin(x):  
    return math.sin((x*math.pi)/180)  
while True:  
    try:  
        line = input() 
        if line.find("<-") != -1:  
            line = line.split("<-")  
            line2 = line[0]+"="+line[1]  
            exec(line2)  
        else:  
            eval(line)  
    except EOFError:  
        break  