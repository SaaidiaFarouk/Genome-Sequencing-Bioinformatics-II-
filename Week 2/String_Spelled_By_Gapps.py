import os 
os.remove("answear.txt")
def stringdevider(pairs):
    list1=[]
    list2=[]
    tpl=tuple()
    for pair in pairs : 
        x=pair.index("|")
        kmer1=pair[0:x]
        kmer2=pair[x+1:len(pair)]
        list1.append(kmer1)
        list2.append(kmer2)
    tpl=(list1,list2)
    return tpl

def composer(list4):
    str=list4[0]
    t=len(list4[0])
    for i in range(1,len(list4)): 
        str=str+list4[i][t-1]
    return str 
    
def overlapper(pairs,d,k):
    tpl=stringdevider(pairs)
    firstpatterns=tpl[0]
    secondpatterns=tpl[1]
    prefixstring=(composer(firstpatterns))
    suffixstring=(composer(secondpatterns))
    for i in range(k+d+1,len(prefixstring)):
        if prefixstring[i]!=suffixstring[i-k-d]:
            return "There is no string spelels by the gapped patterns"
    genome=prefixstring+suffixstring[len(suffixstring)-(k+d):len(suffixstring)]
    return genome
f=open("dataset.txt","r")
str=f.readline()
list3=str.split(' ')
d=open("answear.txt","a")
d.write(overlapper(list3,3,1))
print(overlapper(list3,3,1))
d.close()
f.close()




