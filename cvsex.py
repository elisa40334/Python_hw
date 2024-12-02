import csv
import random
import numpy as np
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

pt = [Point(np.random.randint(0,1000)-500,np.random.randint(0,1000)-500) for _ in range(100)]

ptt = []
for i in pt:
    ptt.append({'x':i.x,'y':i.y})
with open('points.csv', 'w', encoding='Big5',newline='') as csvfile: # encoding='utf
    fieldnames = ['x','y']
    writer= csv.DictWriter(csvfile, fieldnames=fieldnames, quotechar="'")
    writer.writeheader()
    writer.writerows(ptt) 

with open("points.csv", 'r',encoding='Big5',newline='') as csvfile: # encoding='utf-
    reader=csv.reader(csvfile,delimiter=',', quotechar="'")
    pt2 = [Point(row[0],row[1]) for row in reader]
    
for p in pt2:
    print('x:{} y:{}'.format(p.x,p.y))