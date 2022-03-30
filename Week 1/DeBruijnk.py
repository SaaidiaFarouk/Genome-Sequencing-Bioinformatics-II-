import os 
os.remove("answear.txt")
def DeBruijnk(text,k):
    list1=list()
    for i in range(len(text)-k+2):
        list1.append(text[i:i+k-1])
    list1.sort()
    stuff=dict()
    for i in range(len(list1)):
        stuff.update({list1[i]:[]})
        prefix=list1[i][1:k-1]
        for j in range(len(list1)):
            suffix=list1[j][0:k-2]
            if suffix==prefix:
                stuff[list1[i]].append(list1[j])
    stuf=dict()
    for k,v in stuff.items():
        if v !=[]:
            stuf[k]=v
    return stuf

f=open("dataset.txt",'r')
text=f.read()
d=open('answear.txt','a')
k=4
for k,v in DeBruijnk(text,k).items() :
    d.write(k)
    d.write(': ')
    for n in v:
        d.write(n)
        d.write(" ")
    d.write('\n')
f.close()
d.close()
