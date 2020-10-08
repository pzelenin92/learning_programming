# <a href=.(https?|ftp|www)?(:|\.)?(\/\/)?(\w+.(\w)*.(org|ru|com))
# <a href=.(\w+)?(\W+)?(\w+.(\w)*\.(\w)+)
#<a href=.([A-VX-Za-vx-z]+)?(\W+)?(\w+.(\w)*\.(\w)+)
#<a href=.(https?|ftp)?(\W*)((www\.)?(.*)(\.\w+))
import requests
import re

pattern=r'<a href=(\"|\')((https?|ftp):\/\/)?((www)?(\w+(\.\w*)?)\.(\w+))'
# a=str(input())
#a='http://pastebin.com/raw/2mie4QYa'
# r=requests.get(a)
# string=r.text
#string='<a href="http://stepic.org/courses"><a href="https://stepic.org"><a href="http://neerc.ifmo.ru:1345"><a href="ftp://mail.ru/distib" ><a href="ya.ru"><a href="www.ya.ru"><a href="../skip_relative_links">'
l=[]
finditer_obj=re.finditer(pattern,string)
# for i in finditer_obj:
#     if i.group(1)=='www':
#         c=i.group(1)+i.group(2)+i.group(3)
#         l.append(c)
#     elif i.group(3) not in l:
#         l.append(i.group(3))
for i in finditer_obj:
    c=i.group(4)
    if c not in l:
         l.append(c)
# print(l)
for i in sorted(l):
    print(i)
# for i in finditer_obj:
#     k=0
#     for g in i.groups():
#         print('g',k,'=',g)
#         k+=1
    # print(i.group(0))
    # print(i.group(1))
    # print(i.group(2))
    # print(i.group(3))
    # print(i.group(4))
    # c=i.group(3)
    # if c not in l:
    #      l.append(c)


#    print(i.group(3))
