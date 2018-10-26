
# arr=[[1,'a',3],[3,'b',2],[2,'c',1]]
# arr=sorted(arr,key=lambda x:x[2])
# print(arr)
# for line in enumerate(arr,start=0):
#     print(line[1])

# titles_file=open('new_title.csv','a',encoding='utf-8')
# article_id=100;
# titles=['小宝','宝','大','懵懵']
# for title in titles:
#     line=str(article_id)+','+title+'\n'
#     titles_file.write(line)
# titles_file.close()

str='百度地图下载	{"百度地图下载安装免费": "0.015", "百度地图下载app": "0.002", "百度地图下载手机版": "0.007", "百度地图下载安卓版": "0.003", "百度地图下载安装": "0.090", "百度地图下载安装2017": "0.005", "百度地图下载地图": "0.003", "百度地图下载,": "0.001", "百度地图下载2018": "0.034", "百度地图下载离线地图": "0.002"}	高德地图	应用	0'
arr=str.split('	')
print(arr)