import sys
dict = {'a':'13','b':'22'}
for line in sys.stdin:
    print(line)
    for k,v in dict.items():
        # print("{},{}".format(k,v))
        if line.find(k) != -1:
            line = line.replace(k,v)

    print(line)
