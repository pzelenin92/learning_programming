with open('dataset_24465_4.txt') as idata, open('output.txt', 'w') as odata:
    x=idata.readlines()
    for i in x[::-1]:
        odata.write(i)
