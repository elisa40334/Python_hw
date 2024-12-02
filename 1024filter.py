from functools import reduce
import math

a = list(map(int,input().split(',')))
expr1=filter(lambda x: x % 3 == 0 and x > 0, a)
expr2=map(lambda x:math.exp(-x),a)
expr3=reduce(lambda x,y: abs(x)+abs(y),a)
cmd ='' 
while True:
    try:
        s = input()
        cmd += s+'\n'
    except EOFError:
        break
p = compile(cmd,'default','exec')
exec(p) 