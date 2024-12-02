dict = eval(input())
print(len(dict))
x = int(input())
if x in dict:
    print("True")
else:
    print("False")
x = int(input())
if x not in dict:
    print("Notexisting")
elif dict[x] == 0:
    print("True")
else:
    print("False")
x = eval(input())
dictt = {}
dictt.setdefault(x[0],x[1])
dict.update(dictt)
dicta = sorted(dict)
for i in dicta:
    print(i)
dictb = sorted(dict.items(), key=lambda x:x[1])
for i in dictb:
    print(i[1])
dictc = sorted(dict.items())
for i in dictc:
    print(i)