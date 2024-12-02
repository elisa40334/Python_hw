import re

strr = input()
dict = {"羊":0,"狗":0,"雞":0,"豬":0,"牛":0}
matcha = re.finditer(r"(([豬羊雞狗牛]\d+[隻頭條])|(\d+[隻頭條][豬羊雞狗牛]))",strr)
for i in matcha:
    if i.group()[0].isdigit():
        dict[i.group()[2]] += int(i.group()[0])
    else:
        dict[i.group()[0]] += int(i.group()[1])
    # print(i.group()[0])
# for i in matchb:
#     # dict[i.group()[2]] += int(i.group()[0])
#     print(i.group())
for a,b in dict.items():
    print("{}:{}".format(a,b))