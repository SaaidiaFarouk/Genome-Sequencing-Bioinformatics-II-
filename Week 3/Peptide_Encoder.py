import ast

### Returns the complimentary strand of a DNA
def dnareverter(dna):
    with open("DNA-REV.txt","r") as f:
        data=f.read()
    dnarevdict=ast.literal_eval(data)
    revdna=dna.translate(dnarevdict)
    return revdna

### Reverse transcription of the RNA to DNA
def rnatranscriptor(rna):
    with open("RNA-DNA.txt","r") as f:
        data=f.read()
    rnadnadict=ast.literal_eval(data)
    dna=rna.translate(rnadnadict) 
    return dna

### Returns a list of the codons of a 3->5 RNA (The codons in the list will be in the same order as in the RNA but will be reversed so they can be translated with a uniform database)
def revcodoncomposition(rna):
    txt=rna[::-1]
    codons=list()
    i=0
    while i < len(txt):
        codon=txt[i:i+3]
        i=i+3
        codons.append(codon)
    for codon in codons:
        if len(codon)!=3:
            p=codons.index(codon)
            codons.pop(p)
    return codons[::-1]

### Returns a list of the codons of a 5->3 RNA
def codoncomposition(rna):
    codons=list()
    i=0
    while i < len(rna):
        codon=rna[i:i+3]
        i=i+3
        codons.append(codon)
    if len(codons[len(codons)-1])!=3:
        codons.pop()
    return codons

### Translation of a 5->3 RNA
def rnatranslator(rna,translist):
    prot=''
    codons=codoncomposition(rna)
    for codon in codons : 
        for trans in translist:
            if codon==trans[0]:
                prot=prot+trans[1]
    return prot

### Translation of a 3->5 RNA
def revernatranslator(rna,translist):
    prot=''
    codons=revcodoncomposition(rna)
    for codon in codons : 
        for trans in translist:
            if codon==trans[0]:
                prot=prot+trans[1]
    return prot

### Transcription of a DNA to RNA
def dnatranscriptor(dna):
    with open("DNA-RNA.txt","r") as f:
        data=f.read()
    dnarnadict=ast.literal_eval(data)
    rna=dna.translate(dnarnadict)
    return rna

### All possible codes of a 3->5 RNA with coding for a peptid of thet same lenght as aa
def revsegcomp(rna,aa):
    l=len(aa)*3
    comp=list()
    txt=rna[::-1]
    i=0
    while i < len(txt):
        com=txt[i:i+l]
        i=i+3
        comp.append(com)
    for i in range(len(comp)):
        comp[i]=comp[i][::-1]
    comp=comp[::-1]
    return comp

### All possible codes of a 5->3 RNA with coding for a peptid of thet same lenght as aa
def segcomp(rna,aa):
    l=len(aa)*3
    comp=list()
    i=0
    while i < len(rna):
        com=rna[i:i+l]
        i=i+3
        comp.append(com)
    return comp

### The main function
def peptidencoder(dna,aa):
    substrings=list()
    oa=aa[::-1]
    revdna=dnareverter(dna)
    dnas=(dna,revdna)
    for seq in dnas:
        rna=dnatranscriptor(seq)
        if seq == dna: 
            frames=list()
            frames.append(rna)
            frames.append(rna[:len(rna)-1])
            frames.append(rna[:len(rna)-2])       
            for frame in frames : 
                protsegs=list()
                framesegs=list()
                framesegs=revsegcomp(frame,aa)
                for fseg in framesegs:
                    protsegs.append(revernatranslator(fseg,translist))
                for i in range(len(protsegs)): 
                    if protsegs[i] == oa:
                        substring=framesegs[i]
                        substring=rnatranscriptor(substring)
                        substrings.append(substring)
        elif seq == revdna:
            frames=list()
            frames.append(rna)
            frames.append(rna[1:])
            frames.append(rna[2:])
            for frame in frames:
                framesegs=list()
                protsegs=list()
                framesegs=segcomp(frame,aa)    
                for fseg in framesegs:
                    protsegs.append(rnatranslator(fseg,translist))
                for i in range(len(protsegs)):
                    if protsegs[i] == aa:
                        substring=framesegs[i]
                        substring=rnatranscriptor(substring)
                        substring=dnareverter(substring)
                        substrings.append(substring)
    return substrings

### Creating a list of the genetic Code 
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

### Exctracting data from a dataset
f=open("dataset.txt")
lst=f.readlines()
for i in range(len(lst)):
    lst[i]=lst[i].replace("\n","")
dna=lst[0]
aa=lst[1]


### The program looking for encoding regions in a DNA
substrings=peptidencoder(dna,aa)
with open("answear.txt","w") as d :
    for substring in substrings : 
        d.write(substring +"\n")






