def pretty(a):
    return lambda:'$'+a()+'$'
# @pretty
# def f1():
#   return 'f1'
# print(f1())
# 連同下面程式上載至e-tutor
cmd ='' 
while True:
    try:
        s = input()
        cmd += s+'\n'
    except EOFError:
        break

p = compile(cmd,'default','exec')
exec(p)    
