from itertools import combinations 
c = input() 
 
#將你的運算方式，填入answer字串，使得eval(answer)會得到所欲答案。 
#{} for k in range(len(tt)) tt for i in range(int(ord('A')),int(ord(c))+1) for j in range(i+1),int(ord(c))+1) 
tt = [] 
for i in range(65,int(ord(c))+1): 
    tt.append(chr(i)) 
     
answer = '{x:y for y in range(1,ord(c)-65+2) for x in combinations(tt, y)}'
print(answer) 
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
 