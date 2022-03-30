import os
d=open("answear.txt","a")
d.close()
os.remove("answear.txt")


def codoncomposition(rna):
    codons=list()
    i=0
    while i != len(rna):
        codon=rna[i:i+3]
        i=i+3
        codons.append(codon)
    return codons

def rnatranslator(rna,translist):
    prot=''
    codons=codoncomposition(rna)
    for codon in codons : 
        for trans in translist:
            if codon==trans[0]:
                prot=prot+trans[1]
    return prot

def translister(lst):
    translist=list()
    for line in lst : 
        tpl=tuple()
        lst1=line.split(" ")
        lst1[1]=lst1[1].replace("\n","")
        tpl=(lst1[0],lst1[1])
        translist.append(tpl)
    return translist

v=open("RNA-Codon.txt","r")
lst=v.readlines()
v.close()
translist=translister(lst)

f=open("dataset.txt","r")
rna=f.readline()
f.close()
rna="CCGAGGACCGAAAUCAAC"
prot=rnatranslator(rna,translist)

d=open("answear.txt","a")
d.write(prot)
d.close()