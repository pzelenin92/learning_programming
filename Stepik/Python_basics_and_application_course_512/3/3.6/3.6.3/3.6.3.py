import requests

template="http://numbersapi.com/{}/math"
params={
    "json" : True
    }

with open("dataset_24476_3.txt", "r") as inputdataset:
    for line in inputdataset:
        url=template.format(line.rstrip())
        res=requests.get(url,params=params)
        data=res.json()
        # print(res.url)
        # print(data)
        if data["found"]==True:
            print("Interesting")
        else:
            print("Boring")
