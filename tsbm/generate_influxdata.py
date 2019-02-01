import time
import random

file=open('influx_data.txt','w')
head_line="# DML\n# CONTEXT-DATABASE: ructest4\n"
file.write(head_line)
file.close()
# print(head_line)
start_time=1514736000000
# 2018-01-01 01:00:00
end_time=1514739600000
# end_time=1515340800000
while(start_time<=end_time):
    file = open('influx_data.txt', 'a')
    ds=100
    dn=0
    while(dn<ds):
        ss=150
        sn=0
        while(sn<ss):
            sn=sn+1
            line="sensor,d=d_"+str(dn)+",s=s_"+str(sn)+" value="+str(random.uniform(-100, 100))+"1 "+str(start_time)+'\n'
            # print(line)
            file.write(line)
        dn=dn+1
    file.close()
    start_time=start_time+7000
