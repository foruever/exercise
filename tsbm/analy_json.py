import json

f = open("data/result.opentsdb.json", encoding='utf-8')
w= open('result.opentsdb.csv', 'w')
bodys = json.load(f)
for body in bodys:
    try:
        testMode=body['param_config']['testMode'];
        #print(body['param_config']['backgroupStatus'])
        bg=body['param_config']['backgroupStatus'];
        if('read'==testMode):
            # print(body['result_read'])
            result=body['result_read']
            mean=result['meanTimeout'];
            max=result['maxTimeout'];
            th95=result['ninty5Timeout'];
            th50=result['fiftyTimeout'];
            min=result['minTimeout'];
            tps=result['tps'];
            ratio=result['successRatio'];
            sum_r=result['sumRequests']
            line=str(tps) + ',' + str(mean) + ',' + str(th50) + ',' + str(th95) + ',' + str(max) + ',' + str(
                min) + ',' + str(sum_r) + ',' + str(ratio) + '\n'
            w.write(line)
            # print(str(tps) + ',' + str(mean) + ',' + str(th50) + ',' + str(th95) + ',' + str(max) + ',' + str(
            #     min) + ',' + str(sum_r) + ',' + str(ratio) + '\n')
        if('write'==testMode):
           # print(body['result_write'])
           result = body['result_write']
           mean = result['meanTimeout'];
           max = result['maxTimeout'];
           th95 = result['ninty5Timeout'];
           th50 = result['fiftyTimeout'];
           min = result['minTimeout'];
           pps = result['pps'];
           sum_r = result['sumPoints']
           line=str(pps)+','+str(mean)+','+str(th50)+','+str(th95)+','+str(max)+','+str(min)+','+str(sum_r)+'\n'
           w.write(line)
    except:
        print(body)
       # print(str(pps)+','+str(mean)+','+str(th50)+','+str(th95)+','+str(max)+','+str(min)+','+str(sum_r)+'\n')
f.close()
w.close()