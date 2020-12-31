# l1=[4,7]
# l2=[1,3]
# l3=[2,5]
# l4=[5,6]
#
# l=[l1,l2,l3,l4]
n=int(input())
l=[]
i=0
while i<n:
    l.append([int(i) for i in input().split()])
    i+=1
# print(l)

l.sort(key=lambda x:x[1])

point=[l[0][1]]

for section in l[1:]:
    if section[0]>point[-1:][0]:
        point.append(section[1])

print(len(point))
for i in point:
    print(i,end=' ')

