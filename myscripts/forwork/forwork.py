import csv
import os

workers = [
    ["Maxim",0],
    ["Pavel",0],
    ["Ivan",1,"4е ноября"],
    ["Andrei",1,"4е ноября"]
]
header = [
    ["Name","Counter","Holidays"]
]
data = []
x = "test1.csv"

if x in os.listdir():
    #считываем файл
    with open ("test1.csv",'r',newline='') as testfile:
        reader=csv.reader(testfile)
    #собираем дату в лист
        l=[]
        for row in reader:
            l.append(row)
        print(l)


else:
    #создаем файл и запишем туда обработанную дату
    with open ("test1.csv",'w',newline='') as testfile:
        writer=csv.writer(testfile)
        #запишем дату
        writer.writerows(workers)






