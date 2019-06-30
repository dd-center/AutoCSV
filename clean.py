import os
import re
# uid = ['368082','21233113','596082','9858137','38041','74644','4657471','13307515','6304558','10571456','21143293','14410598','21334538','9079110','13431737','135395','10068416','10358807','24276','3602205','850447','2077667']
# for k in range(len(uid)):
#     filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/2019-05-12'
#     length = len([name for name in os.listdir(filedir) if os.path.isfile(os.path.join(filedir, name))])
#     for i in range(length):
#         with open(filedir+"/bundle"+str(i),"r",encoding='utf_8') as f:
#                 raw = f.read()
#         os.remove(filedir+"/bundle"+str(i))
#         with open(filedir+"/total","a",encoding='utf-8') as f:
#             f.write(raw)
#     with open(filedir+"/total","a",encoding='utf-8') as f:
#         f.write("\"type\":\"online\",\"total\":1}")
#         print(str(uid[k])+" OK")

uid = ['12235923','14917277','14222920','14578426','13946381','337374','3822389','4895312','7962050','11575621','21288388','13576775','14275133','21133979','14110147','1321846','14052636','21224291','3889934','14327465','14893','596082','6241497','11588230','12770821','160683','919919','10209381','21302352','947447','21130785','21302479','21195793','4664126','15142311','21320551','21304638','3827429','21302477','6632844','21107534','21318294','4634167','21132965','21219990','21144047','21131813','21302469','15065340','21317030','9680769','180784','21300316','8725120','21320281','284685','262755','895206','278936','21357592','13289738','3657657','21233113','14892076','6080883','21129632','7688266','6304558','2077667','13744134','135395','21327595','11110277','10571456','38041','13431737','21334538','6586670','2610619','24276','74644','11261960','704808','368082','9858137','40529','4078398','12492310','4657471','13307515','21143293','14410598','9079110','10068416','10358807','3602205','850447','21470454','21420932','566227','21425985']
for k in range(len(uid)):
        filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/2019-06-02'
        length = len([name for name in os.listdir(filedir) if os.path.isfile(os.path.join(filedir, name))])
        for i in range(length):
            with open(filedir+"/bundle"+str(i),"r",encoding='utf_8') as f:
                    raw = f.read()
            os.remove(filedir+"/bundle"+str(i))
            with open(filedir+"/total","a",encoding='utf-8') as f:
                f.write(raw)
        with open(filedir+"/total","a",encoding='utf-8') as f:
            f.write("\"type\":\"online\",\"total\":1}")
# for k in range(len(uid)):
#     cleandir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/2019-05-10'
#     os.remove(cleandir+"/total")
#     print(str(uid[k])+" OK")
# filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/21133979/2019-05-17"
# resultdir = "C:/Users/Administrator/Documents/blive/"
# with open(filedir+"/total","r",encoding='utf-8') as f:
#         raw = f.read()
# rawcomment = re.findall(r"(\"comment\":\".{1,100}\",\"user\":{\"id\":\d*,\"name\":\".{1,40}\",\"is)",raw)
# with open(resultdir+"mio0517.txt","a",encoding='utf_8_sig') as f:
#         f.write(str(rawcomment))