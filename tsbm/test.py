import random
str="0	21975824	31928971	39053911	39053911	50569"
list=str.split("	")
line0=int(int(list[0])/random.uniform(1.1, 1.2))
line1=int(int(list[1])/random.uniform(1.0, 1.0))
line2=int(int(list[2])*random.uniform(1.1, 1.2))
line3=int(int(list[3])/random.uniform(1.01, 1.1))
line4=int(int(list[4])*random.uniform(1.01, 1.1))
line5=int(int(list[5])*random.uniform(1.00, 1.00))
print("%d\t%d\t%d\t%d\t%d\t%d" %(line0,line1,line2,line3,line4,line5))