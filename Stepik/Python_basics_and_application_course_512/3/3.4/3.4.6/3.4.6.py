import requests
import re

def poisk(a):
    r=requests.get(a)
    string=r.text
    findall_obj=re.findall(pattern,string)
    return findall_obj #return a list of links from the web page A

pattern=r'https:.*html'
counter=0
a,b=(str(input()) for k in range(2))
# a='https://stepic.org/media/attachments/lesson/24472/sample1.html'
# b='https://stepic.org/media/attachments/lesson/24472/sample2.html'
for i in poisk(a):
    if b in poisk(i):
        counter+=1 #+1 если совершился двойной переход
    else:
        continue

if counter>0:
    print('Yes')#если был совершен хотя бы один двойной переход, то принтуем "Yes"
else:
    print('No')
