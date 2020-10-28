import csv
import os

#0 ввод новых данных с консоли и запись их для дальнейшей обработки
xnewdata=[]
print("введите новые значения в формате: 'Имя, Праздник' через запятую затем нажмите enter. Когда закончите вводить наберите 'stop'")
while True:
    newdata=input().split(',')
    for i in range(len(newdata)):
        newdata.insert(i,newdata.pop(i).strip().lower())
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
print('xnewdata= ',xnewdata)

#обработка полученных данных - приведение к формату {Name:{Holiday:Count}} ПЕРЕДЕЛАТЬ так же как и на считывании из файла
dinput = {}

if len(xnewdata) != 0:
    for i in xnewdata:
        if i[0] in dinput:
            dinput[i[0]][i[1]]+=1
        else:
            dinput[i[0]] = {i[1]:1}
    print('dinput= ',dinput)
else:
    print('dinput= ',dinput, "Ни одного значения не введено")

#1 проверка на наличие старого файла в текущей директории для сбора оттуда даты
x = "test1.csv"
if x in os.listdir():
    #1 считываем файл который есть в директории
    with open ("test1.csv",'r',newline='') as testfile:
        reader=csv.reader(testfile)
    #1.2 собираем дату в лист
        l=[]
        for row in reader:
            k = []
            for i in row:
                istrip = i.strip()
                if istrip in ['Name','Counter','Holidays']:
                    print("pidor")
                else:
                    k.append(istrip)
            if k != []:
                l.append(k)
        print('l= ',l)
    #1.3 обработка полученных данных - приведение к формату {Name:[count,[Holiday]]}
    dl = {}
    if len(l) != 0:
        for i in l:
            if i[0] in dl:
                dl[i[0]][0]+=1
                dl[i[0]][1].extend(i for i in i[2:])
            else:
                dl[i[0]] = [int(i[1]),i[2:]]
        print('dl= ',dl)
    else:
        print('dl= ',dl, "Ни одного значения не получено")

# #создаем файл и запишем туда сначала хедер
# with open ("test1.csv",'w',newline='') as testfile:
#     header=["Name","Counter","Holidays"]
#     writer=csv.writer(testfile)
#     #запишем дату
#     writer.writerows(header)




