from copy import deepcopy
import random 

def randonumberexept(l,n):
    y=n
    while y==n:
        y = random.randint(0, l)
    return y

def graphcomposition(Graph):
    composition=list()
    for key in Graph.keys():
        composition.append(key)
    for val in Graph.values():
        for node in val :
            if node not in composition:
                composition.append(node)
    return composition

def outdegree(node,Graph):
    if node not in Graph.keys():
        outdeg=0
    else:
        outdeg=len(Graph[node])
    return outdeg

def indegree(node,Graph):
    indeg=0
    for nide in Graph.values():
        for part in nide:
            if part==node:
                indeg=indeg+1
    return indeg

def cyclecreator(Graph):
    end=''
    start=''
    composition=graphcomposition(Graph)
    for node in composition:
        if indegree(node,Graph)>outdegree(node,Graph):
            end=node
        elif outdegree(node,Graph)>indegree(node,Graph):
            start=node
    if end not in Graph.keys() :
        list1=list()
        list1.append(start)
        Graph.update({end:list1})
    elif end!='':
        Graph[end]=start
    return Graph

def endfinder(Graph):
    composition=graphcomposition(Graph)
    end=''
    for node in composition:
        if indegree(node,Graph)>outdegree(node,Graph):
            end=node
    return end 

def startfinder(Graph):
    composition=graphcomposition(Graph)
    start=''
    for node in composition:
        if indegree(node,Graph)<outdegree(node,Graph):
            start=node
    return start

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

def Eulerianpath(graph):
    endstr=endfinder(graph)
    Cycle=[]
    Graph=dict()
    for k,v in graph.items() : 
        j=deepcopy(v)
        Graph.update({k:j})
    lg=getListofvaluess(Graph)
    ststr=startfinder(Graph)
    Graph=cyclecreator(Graph)
        #finding the starting node
    Cycle.append(ststr)
        # adding the second node
    lv=len(Graph[ststr])
    if endstr in Graph[ststr] and len(Graph[endstr])==1:
        p=Graph[ststr].index(endstr)
        lp=lv-1
        sti=randonumberexept(lp,p)
        stistr=Graph[ststr][sti]
        Cycle.append(stistr)
        Graph[ststr].pop(sti)
    else:
        sti=random.randint(0,lv-1)
        stistr=Graph[ststr][sti]
        Cycle.append(stistr)
        Graph[ststr].pop(sti)
            
        #completing the first cycle
    str=stistr
    while Graph[str]!=[] and str!=ststr :
        lv=len(Graph[str])
        if endstr in Graph[str] and len(Graph[endstr])==1:
            p=Graph[str].index(endstr)
            if lv==1:
                sti=0
            if lv!=1:
                lp=lv-1
                sti=randonumberexept(lp,p)
            stistr=Graph[str][sti]
            Cycle.append(stistr)
            Graph[str].pop(sti)
        elif len(Cycle) == lg:
            sti=random.randint(0,lv-1)
            stistr=Graph[str][sti]
            Cycle.append(stistr)
            Graph[str].pop(sti)
        else:    
            sti=random.randint(0,lv-1)
            stistr=Graph[str][sti]
            Cycle.append(stistr)
            Graph[str].pop(sti)
        str=stistr
    length=getListofvaluess(Graph)
        #completing th entire cycle
    while length>0:
        #finding the newstart
        for node in Cycle:
            if Graph[node]!=[]:
                newstart=node
                break
        Cyclee=list()
        pos=Cycle.index(newstart)
        lastpart=Cycle[pos:len(Cycle)]
        firstpart=Cycle[1:pos+1]
        Cyclee=lastpart+firstpart
        #adding randomly for the first time a node 
        lv=len(Graph[newstart])
        if endstr in Graph[newstart] and len(Graph[endstr])==1:
            p=Graph[newstart].index(endstr)
            lp=lv-1
            sti=randonumberexept(lp,p)
            stistr=Graph[newstart][sti]
            Cycle.append(stistr)
            Graph[newstart].pop(sti)
        elif len(Cyclee) == lg:
            sti=random.randint(0,lv-1)
            stistr=Graph[newstart][sti]
            Cyclee.append(stistr)
            Graph[newstart].pop(sti)
        else:
            sti=random.randint(0,lv-1)
            stistr=Graph[newstart][sti]
            Cyclee.append(stistr)
            Graph[newstart].pop(sti)
        str=stistr
            #completing the cycle
        while Graph[str]!=[] and str!=ststr:
            lv=len(Graph[str])
            if endstr in Graph[str] and len(Graph[endstr])==1:
                p=Graph[str].index(endstr)
                lp=lv-1
                sti=randonumberexept(lp,p)
                stistr=Graph[str][sti]
                Cycle.append(stistr)
                Graph[str].pop(sti)
            elif len(Cyclee) == lg:
                sti=random.randint(0,lv-1)
                stistr=Graph[str][sti]
                Cyclee.append(stistr)
                Graph[str].pop(sti)
            else:
                sti=random.randint(0,lv-1)
                stistr=Graph[str][sti]
                Cyclee.append(stistr)
                Graph[str].pop(sti)
            str=stistr
        Cycle=Cyclee
        length=getListofvaluess(Graph)
    Cycle.pop(len(Cycle)-1)
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
answear=Eulerianpath(Graph)
d=open("answear.txt","w")
for val in answear:
    d.write(val)
    d.write(" ")
f.close