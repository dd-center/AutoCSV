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

uid = ['6241497']
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