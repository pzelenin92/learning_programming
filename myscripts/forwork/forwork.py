import csv
import os

def dict_format(input_data):

    global file_in_dir
    dict_output= {}

    if file_in_dir:
        locvar=2
        def f(i):
            return int(i[1])
    else:
        locvar=1
        def f(i):
            return len(i[1:])

    if len(input_data) != 0:
        for i in input_data:
            if i[0] in dict_output:
                dict_output[i[0]][0]+=1
                dict_output[i[0]][1].extend(i for i in i[locvar:])
            else:
                dict_output[i[0]] = [f(i),i[locvar:]]
        print('dict_output= ',dict_output)
    else:
        print('dict_output= ',dict_output, "Ни одного значения не введено")
    return dict_output

def finder(x):
    a=[]
    for j in x:
        if type(j) is list:
            a.extend(finder(j))
        else:
            a.append(j)
    return a

file_in_dir=False

#0 ввод новых данных с консоли и запись их для дальнейшей обработки
read_keyboard=[]
print("введите новые значения в формате: 'Имя, Праздник' через запятую затем нажмите enter. Когда закончите вводить наберите 'stop'")
while True:
    keyboard_input=input().split(',')
    for i in range(len(keyboard_input)):
        keyboard_input.insert(i, keyboard_input.pop(i).strip().lower())
    if 'stop' in keyboard_input:
        if len(keyboard_input) == 1:
            break
        elif 'stop' in keyboard_input[:-1]:
            print("введен 'stop' не на последнем месте")
            continue
        elif 'stop' in keyboard_input[-1]:
            read_keyboard.append(keyboard_input[:-1])
            break
    else:
        if len(keyboard_input) <2:
            print("введено < 2 значений")
            continue
        else:
            read_keyboard.append(keyboard_input)
print('xnewdata= ', read_keyboard)

#обработка полученных данных - приведение к формату {Name:[count,[Holiday]]}
dict_from_keyboard=dict_format(read_keyboard)
# dinput = {}
# if len(xnewdata) != 0:
#     for i in xnewdata:
#         if i[0] in dinput:
#             dinput[i[0]][0]+=1
#             dinput[i[0]][1].extend(i for i in i[1:])
#         else:
#             HolyCounter=len(i[1:])
#             dinput[i[0]] = [HolyCounter,i[1:]]
#     print('dinput= ',dinput)
# else:
#     print('dinput= ',dinput, "Ни одного значения не введено")

#1 проверка на наличие старого файла в текущей директории для сбора оттуда даты
filename = "test1.csv"
if filename in os.listdir():
    file_in_dir=True
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
    dict_from_csv=dict_format(l)
    # dl = {}
    # if len(l) != 0:
    #     for i in l:
    #         if i[0] in dl:
    #             dl[i[0]][0]+=1
    #             dl[i[0]][1].extend(i for i in i[2:])
    #         else:
    #             dl[i[0]] = [int(i[1]),i[2:]]
    #     print('dl= ',dl)
    # else:
    #     print('dl= ',dl, "Ни одного значения не получено")

    #1.4 merge словари dinput u dl в новый словать d2
    d2={}# Не работает вариант когда в текстовом файле и на входе разные словари
    if len(dict_from_csv) != 0:
        for kd in dict_from_csv:
            if kd in dict_from_keyboard:
                c= dict_from_keyboard[kd][0] + dict_from_csv[kd][0]
                dap= dict_from_csv[kd][1] + dict_from_keyboard[kd][1]
                d2[kd]=[c,dap]
            else:
                d2[kd]=dict_from_csv[kd]
        print('d2= ',d2)
    else:
        for kd in dict_from_keyboard:
            if kd in dict_from_csv:
                c= dict_from_csv[kd][0] + dict_from_keyboard[kd][0]
                dap= dict_from_keyboard[kd][1] + dict_from_csv[kd][1]
                d2[kd]=[c,dap]
            else:
                d2[kd]=dict_from_keyboard[kd]
        print('d2= ',d2)

    #1.5 Преобразуем обратно из словаря в строки,
    dconverted=[]
    for i in d2:
        listi=[]
        listi.append(i)
        listi.extend(finder(d2[i]))
        dconverted.append(listi)
    print("dconverted= ", dconverted)
    # 1.6 перезапишем дату в файл
    if len(dconverted) != 0:
        with open ("test1.csv",'w',newline='') as testfile:
            header=["Name","Counter","Holidays"]
            writer=csv.writer(testfile)
            writer.writerow(header)
            for row in dconverted:
                writer.writerow(row)
    else:
        print("Не было получено даты ни с консоли, ни с текстового файла")
else:
    #1.1 преобразуем из словаря в списки
    dconverted=[]
    for i in dict_from_keyboard:
        listi=[]
        listi.append(i)
        listi.extend(finder(dict_from_keyboard[i]))
        dconverted.append(listi)
    print("dconverted= ", dconverted)
    if len(dconverted) != 0:
        with open ("test1.csv",'w',newline='') as testfile:
            header=["Name","Counter","Holidays"]
            writer=csv.writer(testfile)
            writer.writerow(header)
            for row in dconverted:
                writer.writerow(row)
    else:
        print("Не было получено даты с консоли")
