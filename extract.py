# -*- coding: utf-8 -*-
import re
import datetime
import pandas as pd
import os
import numpy as np

def getYesterday(dayb): 
    today=datetime.date.today() 
    oneday=datetime.timedelta(days=dayb) 
    yesterday=today-oneday  
    return yesterday


if __name__ == '__main__':
    uid = ['6241497','12235923','11588230','13946381','14222920','14275133','14917277','21302352','4634167','3822389','21133979','21302477','21304638','21107534','21130785','21132965','14052636','14327465','21302469','7962050','4664126','12770821','21302479','947447','21224291','21195793','14578426','9680769','21219990','21144047','10209381','21131813','21129632','180784','1321846','14892076','11261960','13744134','11110277','6080883','4895312','6632844','11575621','21317030','14893','3889934','337374','3827429','4078398','13576775','15142311','704808']
    # 
    # names = ['白音小雪','12235923神乐咩啊','11588230白上吹雪','13946381夏色祭','14222920Kanna','14275133赤井心','14917277凑阿夸','21302352静凛','4634167犬山玉姬','3822389有栖mana'，‘21133979大神mio’，‘21302477本间向日葵’ 21304638神楽七奈 21107534癒月巧可 21130785百鬼绫目 21132965紫咲诗音 14052636shiori 14327465花園serena 21302469椎名唯华 7962050森永miu 4664126萝卜子 12770821千草hana 21302479绿仙 94744高槻律 21224291安堂inari 21195793mendako 14578426战斗吧歌姬 9680769物述有栖-爱丽丝 21219990亚绮-罗森 21144047樱巫女 10209381田中姬铃木雏 21131813夜空梅露 21129632大空昴 180784千鈴mei 1321846魔宵sakyu 14892076龙胆尊 11261960mugi 13744134天神子兔音 11110277YuNi 6080883笹木咲 4895312Paryi 6632844ENA 11575621陆婉莹 21317030音俣ruka 14893乌拉の帝国 3889934爱夏なつ 337374綾奈なな 3827429心斎桥オクト 4078398來夢めると 13576775Siva_小虾鱼_ 15142311莉姬リジ爱米莉 704808Overidea_China
    yesterday = str(getYesterday(1))
    cleanday = str(getYesterday(3))
    #yesterday = "2019-04-22"
    resultdir = "C:/Users/Administrator/Documents/blive/"
    with open(resultdir+"comments.csv","a",encoding='utf_8_sig') as f:
        f.write(yesterday+',') 
    with open(resultdir+"income.csv","a",encoding='utf_8_sig') as f:
        f.write(yesterday+',') 
    for k in range(len(uid)):
    # k=1
    # k=0
        result = ""
        times = ""
        value = ""
        dhhtimes = ""
        dhhprice = ""
        filedir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/'+yesterday
        cleandir = "C:/Users/Administrator/AppData/Roaming/danmaku/Platforms/bilibili/history/"+uid[k]+'/'+cleanday
        os.remove(cleandir+"/total")
        length = len([name for name in os.listdir(filedir) if os.path.isfile(os.path.join(filedir, name))])
        for i in range(length):
            with open(filedir+"/bundle"+str(i),"r",encoding='utf_8') as f:
                    raw = f.read()
            os.remove(filedir+"/bundle"+str(i))
            with open(filedir+"/total","a",encoding='utf-8') as f:
                f.write(raw)
        with open(filedir+"/total","a",encoding='utf-8') as f:
            f.write("\"type\":\"online\",\"total\":1}")
        with open(filedir+"/total","r",encoding='utf-8') as f:
            raw = f.read()
        # 以下为正则提取
        rawcomment = re.findall(r"\"type\":\"online\",\"total\":\d{2,10}.*?\"type\":\"online\",\"total\":1}",raw)
        raw1 = re.findall(r"(\"comment\":\".{1,100}\",\"user\":{\"id\":\d*,\"name\":\".{1,40}\",)",str(rawcomment))
        raw2 = re.sub(r"\"comment\":\".{1,100}\",\"user\":{\"id\":\d*,\"name\":\"","",str(raw1))
        raw1 = re.sub(r"\'\,\s\'","",str(raw2))   
        raw2 = re.sub(r"\",\'\]","",str(raw1))
        raw1 = re.sub(r"\['","",str(raw2))
        result = re.sub(r"\"","",str(raw1))
        price1 = re.findall(r"\"coinType\":\"gold\",\"name\":\".{1,10}\",\"count\":\d*,\"price\":\d*",raw)
        price2 = re.sub(r"\"coinType\":\"gold\",\"name\":\".{1,10}\",\"count\":","",str(price1))
        rawtimes = re.findall(r"\'\d+,",price2)
        temp1times = re.findall(r"\d+",str(rawtimes))
        temp2times = re.sub(r"\'","",str(temp1times))
        temp1times = re.sub(r"\s","",str(temp2times))
        temp2times = re.sub(r"\[","",str(temp1times))
        times = re.sub(r"\]","",str(temp2times))
        rawvalue = re.findall(r"\:\d+\'",price2)
        temp1value = re.findall(r"\d+",str(rawvalue))
        temp2value = re.sub(r"\'","",str(temp1value))
        temp1value = re.sub(r"\s","",str(temp2value))
        temp2value = re.sub(r"\[","",str(temp1value))
        value = re.sub(r"\]","",str(temp2value))
        rawdhh = re.findall(r"\"level\":\d,\"count\":\d",raw)
        dhhprice1 = re.findall(r"\d,",str(rawdhh))
        dhhprice2 = re.sub(r",\'","",str(dhhprice1))
        dhhprice1 = re.sub(r"\'","",str(dhhprice2))
        dhhprice2 = re.sub(r"\s","",str(dhhprice1))
        dhhprice1 = re.sub(r"\[","",str(dhhprice2))
        dhhprice2 = re.sub(r"\]","",str(dhhprice1))
        dhhprice1 = re.sub(r"1","a",str(dhhprice2))
        dhhprice1 = re.sub(r"3","198",str(dhhprice2))
        dhhprice2 = re.sub(r"2","1998",str(dhhprice1))
        dhhprice = re.sub(r"a","19998",str(dhhprice2))
        dhhtimes1 = re.findall(r"\d\'",str(rawdhh))
        dhhtimes2 = re.sub(r"\"","",str(dhhtimes1))
        dhhtimes1 = re.sub(r"\'","",str(dhhtimes2))
        dhhtimes2 = re.sub(r"\s","",str(dhhtimes1))
        dhhtimes1 = re.sub(r"\[","",str(dhhtimes2))
        dhhtimes = re.sub(r"\]","",str(dhhtimes1))
        if result:
            print(str(uid[k])+" OK")
        else:   
            print(str(uid[k])+" FAIL") 
        #以下为提取信息处理
        raw3 = result.split(",")
        nameresult = pd.Series(raw3)
        namenum = nameresult.drop_duplicates().count()
        times1 = times.split(",")
        timeresult = pd.Series(times1)
        timeresult = pd.to_numeric(timeresult)
        value1 = value.split(",")
        valueresult = pd.Series(value1)
        valueresult = pd.to_numeric(valueresult)
        times2 = dhhtimes.split(",")
        timeresult2 = pd.Series(times2)
        timeresult2 = pd.to_numeric(timeresult2)
        value2 = dhhprice.split(",")
        valueresult2 = pd.Series(value2)
        valueresult2 = pd.to_numeric(valueresult2)
        money = np.sum(valueresult * timeresult) / 1000 + np.sum(valueresult2 * timeresult2)# 打赏
        with open(resultdir+"comments.csv","a",encoding='utf_8_sig') as f:
            f.write(str(namenum)+',')
            if(k==(len(uid)-1)):
                f.write("\n")
        with open(resultdir+"income.csv","a",encoding='utf_8_sig') as f:
            f.write(str('%0.3f' % (money))+',')
            if(k==(len(uid)-1)):
                f.write("\n") 