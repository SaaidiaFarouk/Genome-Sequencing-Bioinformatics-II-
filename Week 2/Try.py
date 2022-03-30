import os 
os.remove("answear.txt")

def compositiongraph(list1):
    k=len(list1[0])
    list2=[]
    for i in range(len(list1)):
        prefix=list1[i][0:k-1]
        suffix=list1[i][1:k]
        x=(prefix,suffix)
        list2.append(x)
    return list2

def debruijn(list1):
    stuff=dict()
    list2=compositiongraph(list1)
    for i in range(len(list2)):
        if list2[i][0] not in stuff.keys():
            stuff[list2[i][0]]=[]
            stuff[list2[i][0]].append(list2[i][1])
        else :
            stuff[list2[i][0]].append(list2[i][1])
    return(stuff)


f=open("dataset.txt","r")
str=f.readline()
lst=str.split(' ')
d=open("answear.txt","a")
for k,v in debruijn(lst).items() :
    d.write(k)
    d.write(': ')
    for n in v:
        d.write(n)
        d.write(' ')
    d.write("\n")
d.close()
f.close()