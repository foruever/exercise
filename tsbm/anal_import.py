# str="12:29:57.656 [main] INFO cn.edu.ruc.CoreBiz - progerss [83/7652],pps [890736 points/s],points [750000,63000000]"
f=open('data/opentsdb_import_1.log','r')
w=open('opentsdb_import_1.end','a')
for line in f:
    if('points/s]' in line):
        list =line.split('pps [')
        list[1].split(' points/s]')[0]
        print(list[1].split(' points/s]')[0])
        w.write(list[1].split(' points/s]')[0]+'\n')
f.close()
w.close()