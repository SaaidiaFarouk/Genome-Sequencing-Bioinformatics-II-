d=open("answear.txt","a")
d.close()
import os 
os.remove("answear.txt")
import random 
def getListofkeys(dict):
    list = []
    for key in dict.keys():
        list.append(key)
    return list

def getListofvalues(dict):
    list = []
    for val in dict.values():
        list.append(val)
        if val==[]:
            list.remove(val)
    return list

def getListofvaluess(dict):
    n=0
    for val in dict.values():
        n=n+len(val)
    return n

def EulerianCycle(Graph):
    Cycle=list()
    lk=len(Graph.keys())
    st=random.randint(0,lk-1)
    keys=getListofkeys(Graph)
    ststr=keys[st]
    Cycle.append(ststr)
    lv=len(Graph[ststr])
    sti=random.randint(0,lv-1)
    stistr=Graph[ststr][sti]
    Cycle.append(stistr)
    Graph[ststr].pop(sti)
    str=stistr
    while Graph[str]!=[]  :
        lv=len(Graph[str])
        sti=random.randint(0,lv-1)
        stistr=Graph[str][sti]
        Cycle.append(stistr)
        Graph[str].pop(sti)
        str=stistr
    length=getListofvaluess(Graph)
    if len(Cycle)==13:
        d=open("answear.txt","a")
        d.close()
    while length>0:
        for node in Cycle:
            if Graph[node]!=[]:
                newstart=node
                break
        Cyclee=list()
        pos=Cycle.index(newstart)
        lastpart=Cycle[pos:len(Cycle)]
        firstpart=Cycle[1:pos+1]
        Cyclee=lastpart+firstpart
        lv=len(Graph[newstart])
        sti=random.randint(0,lv-1)
        stistr=Graph[newstart][sti]
        Cyclee.append(stistr)
        Graph[newstart].pop(sti)
        str=stistr
        while Graph[str]!=[] :
            lv=len(Graph[str])
            sti=random.randint(0,lv-1)
            stistr=Graph[str][sti]
            Cyclee.append(stistr)
            Graph[str].pop(sti)
            str=stistr
        Cycle=Cyclee
        length=getListofvaluess(Graph)
    return Cycle



f=open("dataset.txt","r")
list1=f.readlines()
Graph=dict()
for line in list1 : 
    line=line.replace("\n",'')
    dp=line.find(":")
    pref=line[0:dp]
    list2=line.split(' ')
    Graph.update({pref:[]})
    for i in range(1,len(list2)):
        Graph[pref].append(list2[i])
answear=EulerianCycle(Graph)
d=open("answear.txt","a")
for val in answear:
    d.write(val)
    d.write(" ")
f.close