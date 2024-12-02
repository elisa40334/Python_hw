from itertools import permutations
def stackperm(x):
    a = []
    for i in range(len(x)):
        a = a + [i]
    for i in permutations(a,len(x)):
        #print(i,":")
        i = list(i)
        check = 0
        ans = []
        for j in range(len(x)):
            b = []
            for k in range(j+1,len(x)):
                if(i[j] > i[k]):
                    b += [i[k]]
            #print("check:",b)
            for bb in range(len(b)-1):
                if b[bb] < b[bb+1]:
                    check = 1
                    break
        if check == 0:
            for j in i:
                ans += [x[j]]
            yield ans   

# for idx,i in enumerate(stackperm([1,2,3])):
#     print(idx,i)          
x = input().split(',')    
    
cmd ='' 
while True:
    try:
        s = input()
        cmd += s+'\n'
    except EOFError:
        break

p = compile(cmd,'default','exec')
exec(p)    
