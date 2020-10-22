import requests
import re

pattern=r"<a.*href=(?:\"|')?(?:[-\w]+:\/\/)?([\w]+[\w\d\.-]*)(?:\/|:|'|\")"
a=str(input())
r=requests.get(a)
string=r.text
findall_obj=re.findall(pattern,string)
s={i for i in findall_obj}
l=[i for i in s]
for i in sorted(l):
    print(i)

#код для тестов из текстовых файлов test1,test2,test3
# with open("test3.txt","r") as test1txt:
#     read_data=test1txt.read()
#     findall_obj=re.findall(pattern,read_data)
#     s={i for i in findall_obj}
#     l=[i for i in s]
#     for i in sorted(l):
#         print(i)

"""
Тест1
Адрес - http://pastebin.com/raw/2mie4QYa
Ответы к тесту1:
bya.ru
mail.ru
neerc.ifmo.ru
sasd.ifmo.ru
stepic.org
www.gtu.edu.ge
www.kya.ru
www.mya.ru
www.ya.ru

Тест2
Адрес - http://pastebin.com/raw/hfMThaGb
Ответы к тесту2:
bya-2.ru
bya.ru
mail-2.ru
mail.ru
neerc.ifmo-2.ru
neerc.ifmo.ru
sas-_0123d.ifmo.ru
sasd.ifmo-2.ru
steeeeeeepic.org
stepic-2.org
stepic.org
test.com
www.gtu.edu-2.ge
www.gtu.edu.ge
www.kya-2.ru
www.kya.ru
www.masdaya.ru
www.mya-2.ru
www.ya-2.ru
www.ya.ru

Тест3
Адрес - http://pastebin.com/raw/7543p0ns
Ответы к тесту3:
adworker.ru
banner.rbc.ru
biztorg.ru
blogi.rbc.ru
cnews.ru
consensus.rbc.ru
conv.rbc.ru
credit.rbc.ru
data.rbc.ru
dict.rbc.ru
drinktime.ru
events.cnews.ru
export.rbc.ru
finolymp.ru
gift.cnews.ru
graph.rbc.ru
magazine.rbc.ru
map.rbc.ru
marketing.rbc.ru
memori.ru
otc-pif.rbc.ru
otc-stock.rbc.ru
pda.rbc.ru
pogoda.rbc.ru
portfolio.rbc.ru
quote-otc.rbc.ru
quote.ru
raiting.rbc.ru
rating.rbc.ru
realty.rbc.ru
redir.rbc.ru
rss.rbc.ru
seminar.rbc.ru
spb.rbc.ru
sport.rbc.ru
static.feed.rbc.ru
stock.rbc.ru
style.rbc.ru
ta.rbc.ru
tata.ru
top.rbc.ru
top100.rambler.ru
turbo.ru
tv.rbc.ru
ug.rbc.ru
ulov-umov.ru
videoarchive.rbc.ru
www.5ballov.ru
www.armd.ru
www.autonews.ru
www.biztorg.ru
www.cnews.ru
www.conf.rbc.ru
www.event.rbc.ru
www.iglobe.ru
www.informer.ru
www.ivd.ru
www.liveinternet.ru
www.m-2.ru
www.nashidengi.ru
www.pochta.ru
www.quote.ru
www.quoterate.ru
www.quotetotal.ru
www.rbc.ru
www.rbc.ua
www.rbcdaily.ru
www.rbcinfosystems.com
www.rbcnews.com
www.rbctv.ru
www.refunder.ru
www.salon.ru
www.seminar.rbc.ru
www.top.rbc.ru
www.turbo.ru
www.turist.ru
www.utro.ru
www.worldclass.ru
zoom.cnews.ru﻿
"""
