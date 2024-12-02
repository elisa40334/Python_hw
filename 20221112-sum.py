import re

match = re.finditer(r"\((\d{1,3})(,\d{3})*\)", input())
total = 0
for i in match:
    i = i.group(0).replace("(","").replace(")","").replace(",","")
    total += int(i)
print(total)