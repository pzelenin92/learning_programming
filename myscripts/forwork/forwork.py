import csv
workers = [
    ["Name","Counter","Holidays"],
    ["Maxim",0],
    ["Pavel",0],
    ["Ivan",1,"4е ноября"],
    ["Andrei",1,"4е ноября"]
]

with open ("test1.csv",'r+',newline='') as testfile:
    reader=csv.reader(testfile)
    writer=csv.writer(testfile)
    try:
        next(reader)
    except StopIteration:
        print("file is empy")
        writer.writerow(workers[0])






