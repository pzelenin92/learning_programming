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
        if input_data == read_keyboard:
            print('dict_from_keyboard= ',dict_output)
        else:
            print('dict_from_csv= ',dict_output)
    else:
        if input_data == read_keyboard:
            print('dict_from_keyboard= ',dict_output, "Ни одного значения не введено")
        else:
            print('dict_from_csv= ',dict_output, "Ни одного значения не введено")
    return dict_output

def list_maker(x): #rename loc variables
    a=[]
    for j in x:
        if type(j) is list:
            a.extend(list_maker(j))
        else:
            a.append(j)
    return a

def func_merger(inp_dict_from_csv, inp_dict_from_keyboard):
    loc_dict_merged={}
    loc_dict_merged.update(inp_dict_from_csv)
    for key in inp_dict_from_keyboard:
        if key in loc_dict_merged:
            counter= loc_dict_merged[key][0] + inp_dict_from_keyboard[key][0]
            holidays= loc_dict_merged[key][1] + inp_dict_from_keyboard[key][1]
            loc_dict_merged[key]=[counter, holidays]
        else:
            loc_dict_merged[key]=inp_dict_from_keyboard[key]
    print('dict_merged= ', loc_dict_merged)
    return loc_dict_merged

def list_format(inp_dict):
    loc_dict_to_list=[]
    for i in inp_dict:
        listi=[]
        listi.append(i)
        listi.extend(list_maker(inp_dict[i]))
        loc_dict_to_list.append(listi)
    print("dict_to_list= ", loc_dict_to_list)
    return loc_dict_to_list

def write_to_csv(inp_filename, inp_dict_to_list):
    with open (inp_filename, 'w', newline='') as testfile:
        writer=csv.writer(testfile)
        header=["Name","Counter","Holidays"]
        writer.writerow(header)
        for row in inp_dict_to_list:
            writer.writerow(row)

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
print('read_keyboard= ', read_keyboard)

#обработка полученных данных - приведение к формату {Name:[count,[Holiday]]}
dict_from_keyboard=dict_format(read_keyboard)

#1 проверка на наличие старого файла в текущей директории для сбора оттуда даты
filename = "test1.csv"
if filename in os.listdir():
    file_in_dir=True
    #1 считываем файл который есть в директории
    with open ("test1.csv",'r',newline='') as testfile:
        reader=csv.reader(testfile)
    #1.2 собираем дату в лист
        read_csv=[]
        for row in reader:
            k = []
            for i in row:
                istrip = i.strip().lower()
                if istrip in ['name','counter','holidays']:
                    continue
                else:
                    k.append(istrip)
            if k != []:
                read_csv.append(k)
        print('read_csv= ', read_csv)

    #1.3 обработка полученных данных - приведение к формату {Name:[count,[Holiday]]}
    dict_from_csv=dict_format(read_csv)

    #1.4 merge словари dinput u dl в новый словать d2
    if len(dict_from_csv) != 0 and len(dict_from_keyboard) != 0:# T and T -> T
        dict_merged=func_merger(dict_from_csv,dict_from_keyboard)
    elif len(dict_from_csv) != 0 or len(dict_from_keyboard) != 0:# F or T -> T, T or F -> T
        if len(dict_from_csv) != 0:
            dict_merged=dict_from_csv
        else:
            dict_merged=dict_from_keyboard
    else:# F or F -> F
        dict_merged={}
        print('dict_merged= ',dict_merged, "Словари для merge были пустые")

    #1.5 Преобразуем обратно из словаря во вложенные списки
    dict_to_list=list_format(dict_merged)

    # 1.6 перезапишем дату в файл
    if len(dict_to_list) != 0:
        write_to_csv(filename,dict_to_list)
    else:
        print("Не было получено даты ни с консоли, ни с текстового файла")
else:
    #1.1 преобразуем из словаря в списки
    dict_to_list=list_format(dict_from_keyboard)

    #1.2 запишем дату в файл
    if len(dict_to_list) != 0:
        write_to_csv(filename,dict_to_list)
    else:
        print("Не было получено даты с консоли")
