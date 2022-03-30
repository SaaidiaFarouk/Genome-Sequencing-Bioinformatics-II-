d=open("answear.txt",'a')
d.close()
import os 
os.remove("answear.txt")

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
    print(len(list1))
    return list1

def paireddebruijn(composition):
    stuff=dict()
    list2=pairedcompositiongraph(composition)
    print(list2)
    for pair in list2:
        if pair[0] not in stuff.keys():
            stuff[pair[0]]=list()
            stuff[pair[0]].append(pair[1])
        elif pair[0] in stuff.keys():
            stuff[pair[0]].append(pair[1])
    return stuff
        


f=open("dataset.txt","r")
strr=f.readline()
f.close()
pairslist=strr.split(' ')
d=open("answear.txt","a")
for k,v in paireddebruijn(pairslist).items() :
    stri=''
    stro=''
    a=str(k[0])
    b=str(k[1])
    stri=('('+a+'|'+b+")")
    d.write(stri+': ')
    for n in v:
        stro=''
        a=str(n[0])
        b=str(n[1])
        stro=('('+a+'|'+b+")")
        d.write(stro+' ') 
    d.write('\n')
d.close()




