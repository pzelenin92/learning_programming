#Вывод путей с названиями файлов. В условии задачи это не требуется
import os.path
f=open('output1.txt', 'w')
for root,dirs,files in os.walk('main'):
    l=[]
    for file in files:
        if file.endswith('.py'):
            #print(os.path.join(root,file))
            l.append(os.path.join(root,file)+'\n')
    l1=sorted(l)
    for i in l1:
        f.write(i)
f.close()
