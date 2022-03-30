def graphcomposition(graph):
    composition=list()
    for key in graph.keys():
        composition.append(key)
    for val in graph.values():
        for node in val :
            if node not in composition:
                composition.append(node)
    return composition

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
print(graphcomposition(Graph))
f.close()
