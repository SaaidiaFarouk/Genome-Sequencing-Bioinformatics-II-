import os 
os.remove("answear.txt")
def pairedcomposition(text,k,d):
    tpl=tuple()
    kmer1=''
    kmer2=''
    composition=[]
    for i in range(len(text)-3*k+d):
        kmer1=text[i:i+k]
        kmer2=text[i+k+d:i+2*k+d]
        tpl=(kmer1,kmer2)
        composition.append(tpl)
    return composition 


text="TAATGCCATGGGATGTT"
k=3
d=2
list1=pairedcomposition(text,k,d)
list1.sort()
print(list1)
d=open("answear.txt","a")
for pair in list1:
    a=str(pair[0])
    b=str(pair[1])
    stri=(''+a+'|'+b+" ")
    print(stri)
    d.write(stri)
d.close()