import datetime
d = datetime.datetime.now()
if d.month<10:
    now_day='0'+str(d.month)
print(d.year,now_day,d.day,sep='-')