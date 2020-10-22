import os.path
f=open('output.txt', 'w')
for root,dirs,files in os.walk('main'):
    l=[]
    for file in files:
        if file.endswith('.py'):
            if root+'\n' not in l:
            # print(os.path.join(root))
                l.append(os.path.join(root)+'\n')
    for i in l:
        f.write(i)
f.close()
