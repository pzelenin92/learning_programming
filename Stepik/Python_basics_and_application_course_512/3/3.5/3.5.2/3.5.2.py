import csv
d = {}
with open("Crimes.csv", "r") as crimescsv:
    dr = csv.DictReader(crimescsv)
    for i in dr:
        if "2015" in i["Date"]:  # фильтруем по году
            if i['Primary Type'] not in d:
                d[i['Primary Type']] = 0
            else:
                d[i['Primary Type']] += 1
# нахождение максимума
m = 0
otvet = ""
for k, v in d.items():
    if v >= m:
        m = v
        otvet = k
print(otvet)
