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

# uid = ['12235923','11588230','13946381','14222920','14917277','3822389','21302477','21304638','21130785','14578426','14893','337374','14275133','21302352','21144047','1321846','14892076','13576775','6241497','21133979','14052636','21224291','21195793','21219990','10209381','21129632','21107534','21132965','14327465','7962050','21302479','947447','6080883','4895312','21317030','3889934','15142311','4634167','21131813','6632844','4664126','12770821','11575621','704808','21302469','180784','3827429','9680769','11261960','4078398','13744134','11110277','21320551','21320281','8725120','262755','3657657','160683','7688266','6586670','278936','12492310','2610619','21318294','13289738','40529','21327595','21357592','284685','14110147','21288388','919919','895206','21300316','15065340']

# for k in range(len(uid)):
#     cleandir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/2019-05-10'
#     os.remove(cleandir+"/total")
#     print(str(uid[k])+" OK")
filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/21133979/2019-05-17"
resultdir = "C:/Users/Administrator/Documents/blive/"
with open(filedir+"/total","r",encoding='utf-8') as f:
        raw = f.read()
rawcomment = re.findall(r"(\"comment\":\".{1,100}\",\"user\":{\"id\":\d*,\"name\":\".{1,40}\",\"is)",raw)
with open(resultdir+"mio0517.txt","a",encoding='utf_8_sig') as f:
        f.write(str(rawcomment))