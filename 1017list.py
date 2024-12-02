list1 = list(map(int,input().split(',')))
num = []
for i in range(0,len(list1)):
    print(str(i)+":"+str(list1[i]),end = '')
    if list1[i] != list1[len(list1)-1]:
        print(",",end='')
list2 = [a for a in list1 if a < 0]
list1 = [a for a in list1 if a >= 0]
print("\n",end='')
# print(list2)
for a,b in zip(list1,list2):
    print(str(a)+":"+str(b),end = '')
    if int(a) != int(list1[len(list1)-1]) and int(b) != int(list2[len(list2)-1]):
        print(",",end='')
print("\n",end='')
# print(list2[len(list2)-1])