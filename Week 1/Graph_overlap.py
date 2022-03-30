import os
d=open("answear.txt","a")
d.close()
os.remove("answear.txt")
def graphoverlap(list1):
    k=len(list1[0])
    stuff=dict()
    for i in range(len(list1)):
        stuff.update({list1[i]:[]})
        prefix=list1[i][1:k]
        for j in range(len(list1)):
            suffix=list1[j][0:k-1]
            if suffix==prefix and list1[j] not in stuff[list1[i]]:
                stuff[list1[i]].append(list1[j])
    stuf=dict()
    for k,v in stuff.items():
        if v !=[]:
            stuf[k]=v
    return stuf

f=open("dataset.txt",'r')
str=f.read()
list=str.split(' ')
list.sort()
d=open('answear.txt','a')
for k,v in graphoverlap(list).items() :
    d.write(k)
    d.write(': ')
    for n in v:
        d.write(n)
        d.write(' ')
    d.write('\n')

f.close()
d.close()