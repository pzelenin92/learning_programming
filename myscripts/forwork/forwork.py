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
        elif 'stop' in newdata[:-1]:
            print("введен 'stop' не на последнем месте")
            continue
        elif 'stop' in newdata[-1]:
            xnewdata.append(newdata[:-1])
            break
    else:
        if len(newdata) <2:
            print("введено < 2 значений")
            continue
        else:
            xnewdata.append(newdata)
print('xnewdata= ',xnewdata)

#обработка полученных данных - приведение к формату {Name:{Holiday:Count}} ПЕРЕДЕЛАТЬ так же как и на считывании из файла
dinput = {}
if len(xnewdata) != 0:
    for i in xnewdata:
        if i[0] in dinput:
            dinput[i[0]][0]+=1
            dinput[i[0]][1].extend(i for i in i[1:])
        else:
            HolyCounter=len(i[1:])
            dinput[i[0]] = [HolyCounter,i[1:]]
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
                istrip = i.strip().lower()
                if istrip in ['name','counter','holidays']:
                    continue
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
    #1.4 merge словари dinput u dl в новый словать d2
    d2={}
    for kd in dl:
        if kd in dinput:
            c=dinput[kd][0]+dl[kd][0]
            dap=dl[kd][1]+dinput[kd][1]
            d2[kd]=[c,dap]
        else:
            d2[kd]=dl[kd]
    print('d2= ',d2)
    #1.5 Преобразуем обратно из словаря в строки,

    #1.6 перезапишем дату в файл
    # with open ("test1.csv",'w',newline='') as testfile:
    #     header=["Name","Counter","Holidays"]
    #     writer=csv.writer(testfile)
    #     writer.writerows(header)
# #создаем файл и запишем туда сначала хедер
# with open ("test1.csv",'w',newline='') as testfile:
#     header=["Name","Counter","Holidays"]
#     writer=csv.writer(testfile)
#     #запишем дату
#     writer.writerows(header)




