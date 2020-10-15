from xml.etree import ElementTree

#блок для ввода из файла
# xmldata=ElementTree.parse("example.xml")
# root=xmldata.getroot()
# xmldatastr=ElementTree.tostring(root) #для перевода в стрингу xmldata для обработки в xmlparser
# print(xmldatastr)

xmldatastr='<cube color="blue"><cube color="red"></cube><cube color="red"><cube color="green"></cube></cube></cube>'
# xmldatastr=str(input())
class pparser:
    d,level,r,g,b={},0,0,0,0
    def start(self,tag,attrib):
        self.level+=1
        if self.level not in self.d:
            self.d[self.level]=[]
            self.d[self.level].append(attrib['color'])
        else:
            self.d[self.level].append(attrib['color'])
    def end(self,tag):
        self.level-=1
    def data(self,data):
        pass
    def close(self):
        for i in self.d:
            self.r+=i*self.d[i].count('red')
            self.g+=i*self.d[i].count('green')
            self.b+=i*self.d[i].count('blue')
        return print(self.d, self.r, self.g, self.b)
target=pparser()
parser=ElementTree.XMLParser(target=target)
parser.feed(xmldatastr)
parser.close()

