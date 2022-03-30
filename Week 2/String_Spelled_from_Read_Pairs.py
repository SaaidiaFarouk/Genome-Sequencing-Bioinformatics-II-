import random 
from copy import deepcopy

### Paired DeBruijn Graph

def pairedcompositiongraph(composition):
    comp=list()
    for pir in composition:
        tpl=tuple()
        x=pir.index("|")
        kmer1=pir[0:x]
        kmer2=pir[x+1:len(pir)]
        tpl=(kmer1,kmer2)
        comp.append(tpl)
    k=len(comp[0][1])
    list1=list()
    for pair in comp : 
        prefix=tuple()
        suffix=tuple()
        prefix=(pair[0][0:k-1],pair[1][0:k-1])
        suffix=(pair[0][1:k],pair[1][1:k])
        x=(prefix,suffix)
        list1.append(x)
    return list1

def paireddebruijn(composition):
    stuff=dict()
    list2=pairedcompositiongraph(composition)
    i=0
    for pair in list2:
        if pair[0] not in stuff.keys():
            stuff[pair[0]]=list()
            stuff[pair[0]].append(pair[1])
        elif pair[0] in stuff.keys():
            stuff[pair[0]].append(pair[1])
    return stuff

### Eulerian Cycle

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
        d.write("genius")
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

### Eulerian Path

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
    elif end in Graph.keys():
        Graph[end].append(start)
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

### Overlapper

def cyclecheck(graph):
    val=True
    for pair in graphcomposition(graph):
        if indegree(pair,graph)!=outdegree(pair,graph):
            val=False
    return val

def composer(list4):
    str=list4[0]
    t=len(list4[0])
    for i in range(1,len(list4)): 
        str=str+list4[i][t-1]
    return str 

def overlapper(pairedgraph,d,k):
    if cyclecheck(pairedgraph)==True:
        eulpath=EulerianCycle(pairedgraph)
    elif cyclecheck(pairedgraph)==False:    
        eulpath=Eulerianpath(pairedgraph)
    firstpatterns=[]
    secondpatterns=[]
    for tpl in eulpath:
        firstpatterns.append(tpl[0])
        secondpatterns.append(tpl[1])
    prefixstring=composer(firstpatterns)
    suffixstring=composer(secondpatterns)
    for i in range(k+d+1,len(prefixstring)):
        if prefixstring[i]!=suffixstring[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    genome=prefixstring+suffixstring[len(suffixstring)-k-d:]
    return genome
    





f=open("dataset.txt","r")
pairlist=[]
str=f.readline()
pairslist=str.split(' ')
graph=paireddebruijn(pairslist)
k=3
b=1
ans=overlapper(graph,b,k)
print(ans)

with open("answear.txt","w") as d:
    d.write(ans)

f.close()