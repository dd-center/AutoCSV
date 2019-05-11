import os

uid = ['21320551','21320281','8725120','262755','3657657','160683','7688266','6586670','278936','12492310','2610619','21318294','13289738','40529','21327595','21357592','284685','14110147','21288388','919919','895206','21300316','15065340']
for k in range(len(uid)):
    filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/2019-05-10'
    length = len([name for name in os.listdir(filedir) if os.path.isfile(os.path.join(filedir, name))])
    for i in range(length):
        with open(filedir+"/bundle"+str(i),"r",encoding='utf_8') as f:
                raw = f.read()
        os.remove(filedir+"/bundle"+str(i))
        with open(filedir+"/total","a",encoding='utf-8') as f:
            f.write(raw)
    with open(filedir+"/total","a",encoding='utf-8') as f:
        f.write("\"type\":\"online\",\"total\":1}")
        print(str(uid[k])+" OK")