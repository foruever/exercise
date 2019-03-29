import json

with open('data/opentsdb_data_write') as f:
    lines = f.readlines()
    for line in lines:
        j={"param_config":{"backgroupStatus":1,"batchCode":"V1_opentsdb_write_1","cacheTimes":1,"constantRatio":0.352,"deviceNum":50,"endTime":1517414470000,"lineRatio":0.054,"loseRatio":0.0,"randomRatio":0.512,"readAggreRatio":0.1,"readClients":180,"readHighRatio":0.0,"readPeriod":5,"readPulse":50,"readShrinkRatio":0.1,"readSimpleRatio":0.8,"sensorNum":150,"sinRatio":0.036,"squareRatio":0.054,"startTime":1517414400000,"step":7000,"testMode":"write","writeClients":1,"writePulse":500},"result_write":{"batchCode":"V1_opentsdb_write_1","endTime":1543487739797,"fiftyTimeout":6546,"maxTimeout":78652,"meanTimeout":20034,"minTimeout":5961,"ninty5Timeout":78652,"pps":1071,"startTime":1543487669700,"sumPoints":75000},"data_source":{"batchCode":"V1","dbType":"opentsdb","driverClass":"cn.edu.ruc.adapter.OpentsdbAdapter","ip":"127.0.0.1","passwd":"root","port":"4242","user":"root"}}
        values = line.split('	')
        batch_code='V1_opentsdb_write_'+values[0]
        j['param_config']['batchCode'] = batch_code
        j['result_write']['batchCode'] = batch_code
        j['result_write']['pps'] = values[1]
        j['result_write']['meanTimeout'] = values[2]
        j['result_write']['fiftyTimeout'] = values[3]
        j['result_write']['ninty5Timeout'] = values[4]
        j['result_write']['maxTimeout'] = values[5]
        j['result_write']['minTimeout'] = values[5]
        j['result_write']['sumPoints'] = int(values[0])*75000
        print(json.dumps(j)+",")
with open('data/opentsdb_data_read') as f:
    lines = f.readlines()
    for line in lines:
        j={"result_read":{"batchCode":"V1_opentsdb_read_1","endTime":1543476615831,"fiftyTimeout":17368875,"maxTimeout":17368875,"meanTimeout":17368875,"minTimeout":17368875,"ninty5Timeout":17368875,"startTime":1543476598355,"successRatio":1.0,"sumRequests":1,"tps":0},"param_config":{"backgroupStatus":1,"batchCode":"V1_opentsdb_read_1","cacheTimes":1,"constantRatio":0.352,"deviceNum":100,"endTime":1514995200000,"lineRatio":0.054,"loseRatio":0.0,"randomRatio":0.512,"readAggreRatio":0.1,"readClients":1,"readHighRatio":0.0,"readPeriod":5,"readPulse":50,"readShrinkRatio":0.1,"readSimpleRatio":0.8,"sensorNum":30,"sinRatio":0.036,"squareRatio":0.054,"startTime":1514736000000,"step":7000,"testMode":"read","writeClients":1,"writePulse":500},"data_source":{"batchCode":"V1","dbType":"opentsdb","driverClass":"cn.edu.ruc.adapter.OpentsdbAdapter","ip":"127.0.0.1","passwd":"root","port":"4242","user":"root"}}
        values = line.split('	')
        batch_code='V1_opentsdb_read_'+values[0]
        j['param_config']['batchCode'] = batch_code
        j['result_read']['batchCode'] = batch_code
        j['result_read']['rps'] = values[1]
        j['result_read']['meanTimeout'] = values[2]
        j['result_read']['fiftyTimeout'] = values[3]
        j['result_read']['ninty5Timeout'] = values[4]
        j['result_read']['maxTimeout'] = values[5]
        j['result_read']['minTimeout'] = values[5]
        # j[0]['result_read']['sumPoints'] = int(values[0])*75000
        print(json.dumps(j)+',')
