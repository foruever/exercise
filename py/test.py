a2013=3983.1;
a2014=4449.2
a2015=4969.7
a2016=5541.1
a2017=6170.5
a2018=6807.6
def cal(start,end):
    end=(end-start)/start;
    return end;
print(cal(a2013,a2014))
print(cal(a2014,a2015))
print(cal(a2016,a2017))
print(cal(a2017,a2018))

def sum(a,b,c):
    print(a+b+c)
    return a+b+c
q4=sum(1129,1116,996)
q1=sum(1022,929,1026)
q2=sum(938,1018,886)
q3=sum(923,924,768)
def calJ(start,end):
    return end-start
print(calJ(q4,q1))
print(calJ(q1,q2))
print(calJ(q2,q3))
sumr =q1+q2+q3+q4;
sumc=2.2+2.0+1.9+1.9+2.2+1.6+1.7+1.5+1.5+1.5+1.3;
print(sumc/sumr)
