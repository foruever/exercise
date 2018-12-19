import time
import datetime

ratio=1.0001
print("%.4f" %(ratio**365))
now = datetime.datetime.now()
nowDate = now.strftime("%Y-%m-%d ")
clients=[1,3,5,10,30,50,100,300,500]
#t = time.time()
#start_time = (int(round(t * 1000)))
middle_time=input('请输入起始时间戳！\n')
if(middle_time==None or middle_time==''):
    middle_time='00:00:00';
date_time=time.strptime(nowDate+middle_time, "%Y-%m-%d %H:%M:%S")
print("start datatime :"+nowDate+middle_time)
start_time=int(time.mktime(date_time)*1000)
for client in clients:
    print('WRITE_CLIENTS='+str(client))
    print ('START_TIME='+str(start_time))
    start_time=start_time+70000
    print ('END_TIME='+str(start_time))
    print ('TEST')