import json

#test input
#inp_json='[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
inp_json = '[{"name": "G", "parents" :["F"]}, { "name": "A", "parents": []},{"name" :"B", "parents": ["A"]},{"name": "C", "parents": ["A"]},{"name": "D", "parents": ["B", "C"]},{"name": "E", "parents": ["D"]},{"name": "F", "parents": ["D"]},{"name": "X", "parents": []},{"name": "Y", "parents": ["X", "A"]}, {"name": "Z", "parents": ["X"]},{"name": "V", "parents": ["Z", "Y"]},{"name": "W", "parents": ["V"]}]'

datajsontopy=json.loads(inp_json)
d={}

def foo(x,y):
    if y not in d:
        d[y]=0
    if x not in s: # проверка на наличие в сете для отсеивания лишних прибавлений количества предков
        d[x]+=1
        s.add(x)
    for k in datajsontopy:
        if y in k["parents"]:
            if k["name"] not in s: # проверка на наличие в сете для отсеивания лишних прибавлений количества предков
                d[x]+=1
                s.add(k["name"])
                foo(x,k["name"])

for i in datajsontopy:
    s=set()
    foo(i["name"],i["name"])
for k,v in sorted(zip(d.keys(),d.values())):
    print(k,":",v)
