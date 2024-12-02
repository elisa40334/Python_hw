def distance(p1,p2):
    try:
        return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5
    except AttributeError:
        raise AttributeError
cmd ='' 
while True:
    try:
        s = input()
        cmd += s+'\n'
    except EOFError:
        break

p = compile(cmd,'default','exec')
exec(p)   