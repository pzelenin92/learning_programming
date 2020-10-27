import csv
import os

# workers = [
#     ["Maxim",0],
#     ["Pavel",0],
#     ["Ivan",1,"4е ноября"],
#     ["Andrei",1,"4е ноября"]
# ]
# header = [
#     ["Name","Counter","Holidays"]
# ]
data = []
# x = "test1.csv"

#0 ввод новых данных с консоли и запись их для дальнейшей обработки
xnewdata=[]
print("введите новые значения в формате: 'Имя, Праздник' через запятую затем нажмите enter. Когда закончите вводить наберите 'stop'")
while True:
    newdata=input().split(',')
    for i in range(len(newdata)):
        newdata.insert(i,newdata.pop(i).strip())
    if 'stop' in newdata:
        if len(newdata) == 1:
            break
        elif 'stop' in newdata[:2]:
            print("введен 'stop' на месте одного из элементов: Имя, праздник. Принимается формат: Имя, Праздник")
            continue
        elif 'stop' in newdata[2:]:
            xnewdata.append(newdata[:2])
            break
    else:
        if len(newdata) !=1:
            xnewdata.append(newdata[:2])
        else:
            print("введено одно значение не равное stop, требуется 2: Имя, праздник")
            continue
print(xnewdata)
if len(xnewdata) == 0:
    print("Ни одного значения не введено")
    quit()
'''
#обработка полученных данных - приведение к формату {Name:{Holiday:Count}}
if len(xnewdata) != 0:
    d={xnewdata[0]:{xnewdata[1]:1}}
    print(d)
#1 проверка на наличие старого файла в текущей директории для сбора оттуда даты
if x in os.listdir():
    #1 считываем файл который есть в директории
    with open ("test1.csv",'r',newline='') as testfile:
        reader=csv.reader(testfile)
    #1.2 собираем дату в лист
        l=[]
        for row in reader:
            l.append(row)
        print(l)
    #2 сравниваем data и l
    #2.1  вариант когда data=[] and l=[]
    if data==l:
        with open ("test1.csv",'w',newline='') as testfile:
            writer=csv.writer(testfile)
    #2.2 вариант когда data=[] and l=[...]
        #перенести l in data
        #ввести и обработать input

    #2.3 вариант когда data=[...] and l=[]
        #перенести l in data
        #ввести и обработать input

    #2.4 вариант когда data=[...] and l=[...]

else:
    #создаем файл и запишем туда обработанную дату
    with open ("test1.csv",'w',newline='') as testfile:
        writer=csv.writer(testfile)
        #запишем дату
        writer.writerows(workers)
'''





