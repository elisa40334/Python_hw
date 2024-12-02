class myChain:
    def __init__(self,*a):
        self.a = a
    def __iter__(self):
        for i in range(0,len(self.a)):
            for j in self.a[i]:
                yield j
# c = myChain([1,2,3],[4,5,6],[],[6,7,8])

# # print(len(c.a))
# aa = iter(c)
# for i in c:
#     print(i)
# # for i in range(0,len(c.a)):
# #     for j in c.a[i]:
# #         print(j)
# # print(c.a[0])
# # kk = []
# # for i in c.a:
# #     for j in c.a[i]:
# #         print(j)
# # for i in kk:
# #     print(i)


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