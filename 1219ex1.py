import datetime
from datetime import timedelta
import time
#yyyy-mm-dd hh:mm:ss
# x = input()
# print(x)
# tmstr=time.strftime("%Y-%m-%d %H:%M:%S", x)
x = time.strptime(input(),"%Y-%m-%d %H:%M:%S")
y = time.strptime(input(),"%Y-%m-%d %H:%M:%S")
dayy = abs(datetime.datetime(x.tm_year,x.tm_mon,x.tm_mday,x.tm_hour,x.tm_min,x.tm_sec)-datetime.datetime(y.tm_year,y.tm_mon,y.tm_mday,y.tm_hour,y.tm_min,y.tm_sec)).days
secc = abs(datetime.datetime(x.tm_year,x.tm_mon,x.tm_mday,x.tm_hour,x.tm_min,x.tm_sec)-datetime.datetime(y.tm_year,y.tm_mon,y.tm_mday,y.tm_hour,y.tm_min,y.tm_sec)).seconds
print(dayy,secc)
year=timedelta(days=dayy)
print(int(year.total_seconds()+secc))
# print(x.tm_hour)
# print(y)
# print(datetime.date(2052,2,23))
# print(datetime.datetime(x)-datetime.datetime(y)) 
