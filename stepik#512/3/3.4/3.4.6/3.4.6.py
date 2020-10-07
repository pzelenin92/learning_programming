import requests
import re

def poisk(a):
    r=requests.get(a)
    string=r.text
    findall_obj=re.search(pattern,string)
    group=findall_obj.group(0)
    if group!=b:
        poisk(group)
    else:
        print(group)
        return group


a='https://stepic.org/media/attachments/lesson/24472/sample0.html'
b='https://stepic.org/media/attachments/lesson/24472/sample2.html'

pattern=r'https:.*html'
poisk(a)

# #string=r.text
#
# match_obj=re.match(pattern, string)
# print('match_obj=',match_obj)
#
# findall_obj=re.findall(pattern,string)
# print('findall_obj=',findall_obj)
#
# search_obj=re.search(pattern,string)
# print('search_obj=',search_obj)
#
# fullmatch_obj=re.fullmatch(pattern,string)
# print('fullmatch_obj=',fullmatch_obj)
