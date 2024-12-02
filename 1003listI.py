s = input()
t = input()
print(len(s))#1
print(len(set(s)))#2
list_s = list(s)
print("".join(list_s) )#3
print("".join(sorted(set(s) & set(t))))#4
print(len(set(s) | set(t)))#5
print(len(set(s) - set(t)))#6
x = list(set(s) | set(t))
max = 0
strr  = "a"
for i in range(len(x)):
    if s.count(x[i]) + t.count(x[i]) > max:
        max = s.count(x[i]) + t.count(x[i])
        strr = x[i]
print(strr+":"+str(max))#7