y=open("answear.txt","a")
y.close()
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
    return stuff

def graphmaker(lstt):
    graph=dict()
    for line in lstt:
        line=line.replace('\n','')
        p=line.index(":")
        outer=line[0:p]
        inner=line[p+1:len(line)]
        inner=inner.lstrip()
        innerlst=inner.split(' ')
        graph.update({outer:innerlst})
    return graph

def graphcomposition(graph):
    composition=list()
    for key in graph.keys():
        composition.append(key)
    for val in graph.values():
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

def outgoingedgeslist(node,graph):
    outlst=list()
    for edge in graph[node]:
        tpl=tuple()
        tpl=(node,edge)
        outlst.append(tpl)
    return outlst

def oneinonecheck(node,graph):
    val=False
    ind=indegree(node,graph)
    outd=outdegree(node,graph)
    if ind==outd and ind==1 :
        val=True
    return val

def maximalnonbranchingpaths(graph):
    paths=list()
    composition=graphcomposition(graph)
    for node in composition: 
        valv=oneinonecheck(node,graph)
        if  valv==False:
            if outdegree(node,graph) > 0 :
                for tpl in outgoingedgeslist(node,graph):
                    nonbranchingpath=list()
                    nonbranchingpath.append(tpl[0])
                    nonbranchingpath.append(tpl[1])
                    w=tpl[1]
                    while oneinonecheck(w,graph)==True :
                        u=graph[w][0]
                        nonbranchingpath.append(u)
                        w=u
                    paths.append(nonbranchingpath)
    for node in composition:
        valv=oneinonecheck(node,graph)
        if valv==True:
            if outdegree(node,graph) > 0 :
                for tpl in outgoingedgeslist(node,graph):
                    nonbranchingpath=list()
                    nonbranchingpath.append(tpl[0])
                    nonbranchingpath.append(tpl[1])
                    w=tpl[1]
                    valw=oneinonecheck(w,graph)
                    while valw==True and nonbranchingpath[0]!=nonbranchingpath[len(nonbranchingpath)-1] :
                        u=graph[w][0]
                        nonbranchingpath.append(u)
                        valw=oneinonecheck(u,graph)
                        graph[w].pop()
                        w=u
                if nonbranchingpath[0]==nonbranchingpath[len(nonbranchingpath)-1] :
                    paths.append(nonbranchingpath)
    return paths


    

f=open("dataset.txt","r")
str=f.read()
listo=str.split(' ')
graph=debruijn(listo)
pathss=maximalnonbranchingpaths(graph)
d=open("answear.txt","a")
for path in pathss : 
    st=path[0]
    for i in range(1,len(path)):
        st=st+path[i][len(path[i])-1]
    d.write(st)
    d.write(" ")
f.close()


    