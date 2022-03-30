
def graphcomposition(graph):
    composition=list()
    for key in graph.keys():
        composition.append(key)
    for val in graph.values():
        for node in val :
            if node not in composition:
                composition.append(node)
    return composition

def outdegree(node,graph):
    if node not in graph.keys():
        outdeg=0
    else:
        outdeg=len(graph[node])
    return outdeg

def indegree(node,graph):
    indeg=0
    for nide in graph.values():
        for part in nide:
            if part==node:
                indeg=indeg+1
    return indeg

def cyclecreator(graph):
    end =''
    start=''
    composition=graphcomposition(graph)
    for node in composition:
        if indegree(node,graph)>outdegree(node,graph):
            end=node
            print(end)
        elif outdegree(node,graph)>indegree(node,graph):
            start=node
    if end not in graph.keys() and end!='':
        list1=list()
        list1.append(start)
        graph.update({end:list1})
    elif end!='':
        graph[end]=start
    return graph
    
        

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
print(cyclecreator(Graph))
f.close()

